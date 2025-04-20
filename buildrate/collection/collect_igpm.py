"""
📊 Índice Geral de Preços - Mercado (IGP-M)
📅 Periodicidade: Mensal
🔢 Código SGS: 189
"""

"""
Script para coletar o IGP-M (FGV) mensal via API do Banco Central.
"""

from buildrate.utils.sgs_downloader import baixar_serie_sgs

if __name__ == "__main__":
    baixar_serie_sgs(
        codigo_sgs=189,  # IGP-M mensal (FGV)
        nome_serie="IGP-M",
        salvar_em="data/macro/igpm.csv",
        inicio="01/01/2010"
    )
