#!/usr/bin/env python3
"""manifesto.py - registro e conferência de evidências (manifest.jsonl com SHA-256).

Só biblioteca padrão, Python 3.10+. Não usa rede.
Nunca altera nem apaga arquivo de evidência: lê os arquivos (modo 'rb') e só
ACRESCENTA linhas ao manifest.jsonl da pasta do caso.

Uso:
  python manifesto.py registrar PASTA_DO_CASO ARQUIVO [ARQUIVO...] [opções]
  python manifesto.py conferir  PASTA_DO_CASO

Códigos de saída:
  0  tudo certo
  1  conferir encontrou arquivo divergente, ausente ou linha inválida
  2  erro de uso (pasta, arquivo ou manifesto inválido); nada foi gravado
"""

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
except ImportError:  # pragma: no cover - Python < 3.9 não é suportado
    ZoneInfo = None
    ZoneInfoNotFoundError = KeyError

NOME_MANIFESTO = "manifest.jsonl"
TAMANHO_BLOCO = 1024 * 1024
PADRAO_ID = re.compile(r"^E-(\d+)$")

# Ordem das chaves = ordem do prompt OSINT v5.2, seção 8.
CHAVES = (
    "id", "url", "titulo", "status_http", "coletado_em_brt", "coletado_em_utc",
    "publicado_ou_atualizado_em", "ferramenta", "versao", "plano", "comando",
    "seletor_origem", "sha256", "arquivos", "resultado", "obs",
)


class ErroDeUso(Exception):
    """Erro que impede a operação; nada é gravado."""


# --------------------------------------------------------------------------
# Tempo
# --------------------------------------------------------------------------

def fuso_brasilia():
    """America/Sao_Paulo; se a base de fusos faltar, -03:00 fixo, com aviso."""
    try:
        if ZoneInfo is None:
            raise ZoneInfoNotFoundError("zoneinfo indisponível")
        return ZoneInfo("America/Sao_Paulo")
    except (ZoneInfoNotFoundError, KeyError, ValueError, OSError):
        print(
            "AVISO: base de fusos horários (tzdata) ausente; usando deslocamento "
            "fixo de -03:00 para o horário de Brasília. Para usar America/Sao_Paulo, "
            "instale o pacote: python -m pip install tzdata",
            file=sys.stderr,
        )
        return timezone(timedelta(hours=-3), "BRT")


def agora():
    """Retorna (iso_brt, iso_utc) do mesmo instante, com deslocamento explícito."""
    utc = datetime.now(timezone.utc).replace(microsecond=0)
    brt = utc.astimezone(fuso_brasilia())
    return brt.isoformat(), utc.isoformat()


# --------------------------------------------------------------------------
# Hash e manifesto
# --------------------------------------------------------------------------

def sha256_arquivo(caminho: Path) -> str:
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        for bloco in iter(lambda: f.read(TAMANHO_BLOCO), b""):
            h.update(bloco)
    return h.hexdigest()


def pasta_do_caso(texto: str) -> Path:
    pasta = Path(texto).expanduser()
    if not pasta.is_dir():
        raise ErroDeUso(f"pasta do caso não encontrada: {texto}")
    return pasta.resolve()


def ler_manifesto(caminho: Path):
    """Lê o manifesto. Retorna lista de (numero_da_linha, dict | None, texto_original)."""
    linhas = []
    if not caminho.exists():
        return linhas
    with open(caminho, "r", encoding="utf-8") as f:
        for n, bruto in enumerate(f, start=1):
            texto = bruto.strip()
            if not texto:
                continue
            try:
                obj = json.loads(texto)
                if not isinstance(obj, dict):
                    obj = None
            except json.JSONDecodeError:
                obj = None
            linhas.append((n, obj, texto))
    return linhas


def proximo_id(entradas) -> str:
    maior = 0
    for n, obj, _ in entradas:
        if obj is None:
            raise ErroDeUso(
                f"{NOME_MANIFESTO}, linha {n}: JSON inválido. Corrija ou preserve o "
                "arquivo e comece outro manifesto; o script não grava sobre manifesto corrompido."
            )
        m = PADRAO_ID.match(str(obj.get("id", "")))
        if m:
            maior = max(maior, int(m.group(1)))
    return f"E-{maior + 1:03d}"


def caminho_relativo(arquivo: Path, pasta: Path) -> str:
    """Caminho do arquivo relativo à pasta do caso, com '/' (portável)."""
    try:
        return arquivo.resolve().relative_to(pasta).as_posix()
    except ValueError:
        raise ErroDeUso(f"o arquivo precisa estar dentro da pasta do caso ({pasta}): {arquivo}")


# --------------------------------------------------------------------------
# Subcomando registrar
# --------------------------------------------------------------------------

def cmd_registrar(args) -> int:
    pasta = pasta_do_caso(args.pasta)
    manifesto = pasta / NOME_MANIFESTO

    # Validação completa ANTES de gravar qualquer linha.
    alvos = []
    for texto in args.arquivos:
        arq = Path(texto).expanduser()
        if not arq.is_file() and not arq.is_absolute() and (pasta / arq).is_file():
            arq = pasta / arq  # caminho relativo à pasta do caso, se não existir a partir de onde se está
        if not arq.is_file():
            raise ErroDeUso(f"arquivo não encontrado: {texto}")
        rel = caminho_relativo(arq, pasta)
        if rel == NOME_MANIFESTO:
            raise ErroDeUso("o próprio manifest.jsonl não é evidência a registrar")
        if rel in (r for r, _ in alvos):
            raise ErroDeUso(f"arquivo repetido na linha de comando: {rel}")
        alvos.append((rel, arq))

    if not alvos:
        if args.resultado == "ok":
            raise ErroDeUso("informe ao menos um arquivo (registro sem arquivo só com --resultado vazio, falha ou bloqueada)")
        if not args.obs:
            raise ErroDeUso("registro sem arquivo exige --obs (ex.: 'não encontrado em <fonte>, com <consulta>, em <data>')")

    entradas = ler_manifesto(manifesto)
    ja_registrados = {}
    hashes_vistos = {}
    for _, obj, _ in entradas:
        if obj:
            for a in obj.get("arquivos") or []:
                ja_registrados[a] = obj.get("id")
            if obj.get("sha256"):
                hashes_vistos[obj["sha256"]] = obj.get("id")
    for rel, _ in alvos:
        if rel in ja_registrados:
            raise ErroDeUso(
                f"{rel} já consta como {ja_registrados[rel]}. Evidência registrada não se "
                "re-registra: grave a nova captura com outro nome."
            )

    proximo = proximo_id(entradas)  # valida também o manifesto existente
    numero = int(PADRAO_ID.match(proximo).group(1))
    brt, utc = agora()

    novas = []
    if alvos:
        for rel, arq in alvos:
            digest = sha256_arquivo(arq)
            if digest in hashes_vistos:
                print(f"AVISO: {rel} tem o mesmo SHA-256 de {hashes_vistos[digest]} (conteúdo duplicado).", file=sys.stderr)
            novas.append((f"E-{numero:03d}", digest, [rel]))
            hashes_vistos[digest] = f"E-{numero:03d}"
            numero += 1
    else:
        novas.append((proximo, "", []))

    linhas = []
    for codigo, digest, arquivos in novas:
        registro = {
            "id": codigo,
            "url": args.url,
            "titulo": args.titulo,
            "status_http": args.status_http,
            "coletado_em_brt": brt,
            "coletado_em_utc": utc,
            "publicado_ou_atualizado_em": args.publicado_em,
            "ferramenta": args.ferramenta,
            "versao": args.versao,
            "plano": args.plano,
            "comando": args.comando,
            "seletor_origem": args.seletor_origem,
            "sha256": digest,
            "arquivos": arquivos,
            "resultado": args.resultado,
            "obs": args.obs,
        }
        linhas.append(json.dumps({k: registro[k] for k in CHAVES}, ensure_ascii=False))

    # Única escrita do script: acrescentar ao manifesto.
    precisa_quebra = False
    if manifesto.exists() and manifesto.stat().st_size > 0:
        with open(manifesto, "rb") as f:
            f.seek(-1, 2)
            precisa_quebra = f.read(1) != b"\n"
    with open(manifesto, "a", encoding="utf-8", newline="\n") as f:
        if precisa_quebra:
            f.write("\n")
        for linha in linhas:
            f.write(linha + "\n")

    for codigo, digest, arquivos in novas:
        alvo = arquivos[0] if arquivos else "(sem arquivo)"
        print(f"{codigo}  {digest[:12] or '-' * 12}  {alvo}")
    print(f"{len(novas)} registro(s) acrescentado(s) a {manifesto}")
    return 0


# --------------------------------------------------------------------------
# Subcomando conferir
# --------------------------------------------------------------------------

def cmd_conferir(args) -> int:
    pasta = pasta_do_caso(args.pasta)
    manifesto = pasta / NOME_MANIFESTO
    if not manifesto.exists():
        raise ErroDeUso(f"manifesto não encontrado: {manifesto}")

    entradas = ler_manifesto(manifesto)
    contagem = {"ÍNTEGRO": 0, "DIVERGENTE": 0, "AUSENTE": 0, "SEM ARQUIVO": 0, "INVÁLIDO": 0}

    def informar(estado, codigo, detalhe):
        contagem[estado] += 1
        print(f"{estado:<11}  {codigo:<7}  {detalhe}")

    for n, obj, _ in entradas:
        if obj is None:
            informar("INVÁLIDO", f"l.{n}", "linha que não é um objeto JSON")
            continue
        codigo = str(obj.get("id") or f"l.{n}")
        arquivos = obj.get("arquivos") or []
        esperado = str(obj.get("sha256") or "").lower()
        if not arquivos:
            informar("SEM ARQUIVO", codigo, f"registro sem arquivo (resultado: {obj.get('resultado', '?')})")
            continue
        if len(arquivos) != 1 or not esperado:
            informar("INVÁLIDO", codigo, "esperado exatamente um arquivo e um sha256 por linha")
            continue
        rel = arquivos[0]
        alvo = (pasta / rel)
        try:
            alvo.resolve().relative_to(pasta)
        except ValueError:
            informar("INVÁLIDO", codigo, f"caminho fora da pasta do caso: {rel}")
            continue
        if not alvo.is_file():
            informar("AUSENTE", codigo, rel)
            continue
        achado = sha256_arquivo(alvo)
        if achado == esperado:
            informar("ÍNTEGRO", codigo, rel)
        else:
            informar("DIVERGENTE", codigo, f"{rel}  (manifesto {esperado[:12]}, atual {achado[:12]})")

    problemas = contagem["DIVERGENTE"] + contagem["AUSENTE"] + contagem["INVÁLIDO"]
    resumo = ", ".join(f"{v} {k.lower()}" for k, v in contagem.items() if v)
    print(f"--- {len(entradas)} linha(s): {resumo or 'manifesto vazio'}")
    if problemas:
        print("RESULTADO: HÁ PROBLEMA. Não use os itens divergentes ou ausentes como prova sem explicação documentada.")
        return 1
    print("RESULTADO: todos os arquivos listados conferem com o manifesto.")
    return 0


# --------------------------------------------------------------------------
# Linha de comando
# --------------------------------------------------------------------------

def montar_parser():
    p = argparse.ArgumentParser(
        prog="manifesto.py",
        description="Registra e confere evidências no manifest.jsonl (SHA-256). Sem rede; só acrescenta linhas.",
    )
    sub = p.add_subparsers(dest="comando_", required=True)

    r = sub.add_parser("registrar", help="calcula o SHA-256 de arquivos já gravados na pasta do caso e acrescenta ao manifesto")
    r.add_argument("pasta", help="pasta do caso (a que contém ou conterá o manifest.jsonl)")
    r.add_argument("arquivos", nargs="*", help="arquivos já gravados dentro da pasta do caso (um registro por arquivo)")
    r.add_argument("--url", default="", help="URL de origem")
    r.add_argument("--titulo", default="", help="título da página ou do arquivo")
    r.add_argument("--status-http", type=int, default=None, help="código HTTP observado (inteiro)")
    r.add_argument("--publicado-em", default="", help="data de publicação ou atualização informada pela fonte")
    r.add_argument("--ferramenta", default="", help="ferramenta usada na coleta")
    r.add_argument("--versao", default="", help="versão da ferramenta")
    r.add_argument("--plano", choices=("gratuito", "freemium", "conta"), default="gratuito", help="plano da ferramenta (padrão: gratuito)")
    r.add_argument("--comando", default="", help="comando exato executado (nunca inclua chave ou senha)")
    r.add_argument("--seletor-origem", default="", help="seletor ou E-xxx de onde esta coleta partiu")
    r.add_argument("--resultado", choices=("ok", "vazio", "falha", "bloqueada"), default="ok", help="resultado da coleta (padrão: ok)")
    r.add_argument("--obs", default="", help="observação; no negativo: 'não encontrado em <fonte>, com <consulta>, em <data>'")
    r.set_defaults(func=cmd_registrar)

    c = sub.add_parser("conferir", help="recalcula o SHA-256 de cada arquivo listado e informa íntegro, divergente ou ausente")
    c.add_argument("pasta", help="pasta do caso")
    c.set_defaults(func=cmd_conferir)
    return p


def principal(argv=None) -> int:
    for fluxo in (sys.stdout, sys.stderr):
        try:
            fluxo.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    args = montar_parser().parse_args(argv)
    try:
        return args.func(args)
    except ErroDeUso as e:
        print(f"ERRO: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(principal())
