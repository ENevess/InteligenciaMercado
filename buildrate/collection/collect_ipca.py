"""
📊 Índice de Preços ao Consumidor Amplo (IPCA)
📅 Periodicidade: Mensal
🔢 Código SGS: 433
"""

"""
Script para coletar a série do IPCA mensal via API do Banco Central.
"""

from buildrate.utils.sgs_downloader import baixar_serie_sgs

if __name__ == "__main__":
    baixar_serie_sgs(
        codigo_sgs=433,  # IPCA mensal
        nome_serie="IPCA Mensal",
        salvar_em="data/macro/ipca.csv",
        inicio="01/01/2010"
    )
