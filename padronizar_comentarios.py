import os

# Mapeamento dos arquivos com seus metadados SGS
comentarios_sgs = {
    "collect_usd_brl.py": {
        "descricao": "Cotação de Venda do Dólar (USD/BRL)",
        "periodicidade": "Diária",
        "codigo": 1
    },
    "collect_eur_brl.py": {
        "descricao": "Cotação de Venda do Euro (EUR/BRL)",
        "periodicidade": "Diária",
        "codigo": 21619
    },
    "collect_selic.py": {
        "descricao": "Taxa Selic Meta (mensal)",
        "periodicidade": "Mensal",
        "codigo": 1178
    },
    "collect_cdi.py": {
        "descricao": "Taxa CDI (média diária)",
        "periodicidade": "Diária",
        "codigo": 12
    },
    "collect_ipca.py": {
        "descricao": "Índice de Preços ao Consumidor Amplo (IPCA)",
        "periodicidade": "Mensal",
        "codigo": 433
    },
    "collect_ibcbr.py": {
        "descricao": "Índice de Atividade Econômica (IBC-Br) - dessazonalizado",
        "periodicidade": "Mensal",
        "codigo": 24363
    },
    "collect_igpm.py": {
        "descricao": "Índice Geral de Preços - Mercado (IGP-M)",
        "periodicidade": "Mensal",
        "codigo": 189
    },
    "collect_producao_industrial.py": {
        "descricao": "Produção Industrial Mensal",
        "periodicidade": "Mensal",
        "codigo": 21859
    },
    "collect_exportacoes.py": {
        "descricao": "Exportações de Bens - Conta Corrente",
        "periodicidade": "Mensal",
        "codigo": 22663
    }
}

# Caminho da pasta onde estão os scripts de coleta
base_path = os.path.join(os.path.dirname(__file__), "buildrate", "collection")

# Processar cada arquivo
for nome_arquivo, meta in comentarios_sgs.items():
    caminho = os.path.join(base_path, nome_arquivo)
    if not os.path.exists(caminho):
        continue

    with open(caminho, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    # Evita sobrescrever caso já tenha cabeçalho no formato esperado
    if linhas and linhas[0].startswith('"""📊'):
        continue

    comentario = (
        '"""\n'
        f'📊 {meta["descricao"]}\n'
        f'📅 Periodicidade: {meta["periodicidade"]}\n'
        f'🔢 Código SGS: {meta["codigo"]}\n'
        '"""\n\n'
    )

    novo_conteudo = comentario + "".join(linhas)

    with open(caminho, "w", encoding="utf-8") as f:
        f.write(novo_conteudo)

print("✅ Comentários padronizados adicionados com sucesso.")
