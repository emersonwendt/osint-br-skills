# Como contribuir

Contribuições são bem-vindas, desde que respeitem [ETICA.md](ETICA.md). Ao enviar uma contribuição, você concorda em licenciá-la sob a [licença MIT](LICENSE) deste repositório.

## O que procuramos

- Correção de fontes, links ou referências legais desatualizados.
- Fontes estaduais e municipais (juntas comerciais, geoportais, diários oficiais, tribunais) em arquivos de referência.
- Casos de teste **fictícios** com gabarito.
- Melhorias na `description` que façam a skill ser acionada quando deve.
- Scripts auxiliares simples e auditáveis (ex.: tabela de evidências com SHA-256).

## O que não será aceito

- Dados de casos reais, pessoas identificáveis ou alunos.
- Conteúdo que afrouxe os limites éticos ou ensine técnicas intrusivas.
- Referência legal, jurisprudencial ou doutrinária sem fonte verificável.
- Cópia de material de terceiros sem licença compatível e crédito.

## Ciclo de melhoria

1. **Teste** a skill com um pedido realista e guarde o pedido.
2. **Observe** a falha concreta.
3. **Edite** só o trecho responsável.
4. **Reteste** com o mesmo pedido.
5. **Registre** no `CHANGELOG.md` (seção *Não publicado*).

## Fluxo no GitHub

```bash
# faça um fork no GitHub e depois:
git clone https://github.com/SEU-USUARIO/osint-br-skills.git
cd osint-br-skills
git checkout -b melhoria/descricao-curta
# edite, teste, então:
git add .
git commit -m "skill: o que mudou (teste: pedido usado)"
git push -u origin melhoria/descricao-curta
```

Abra um *pull request* preenchendo o modelo (falha observada, mudança, teste, checagem ética).

## Padrões de escrita das skills

- Português do Brasil, tom técnico, frases curtas.
- `name` em minúsculas com hífens, igual ao nome da pasta; `description` com até ~200 caracteres, dizendo **quando** usar.
- Tabelas "você tem → use → por quê", passos numerados, blocos de comando prontos, lista "onde dá errado".
- Fonte oficial com link; data de verificação para fontes que mudam.
- Material longo em arquivo de referência dentro da pasta da skill (ex.: `referencias/fontes-rs.md`), citado no `SKILL.md`.
- Trechos adaptados de terceiros: manter crédito e atualizar `THIRD_PARTY_NOTICES.md`.

## Revisão

Cada *pull request* é revisado por pelo menos uma pessoa além do autor e pelo mantenedor, com base em: utilidade, precisão, conformidade ética, clareza e rastreabilidade.
