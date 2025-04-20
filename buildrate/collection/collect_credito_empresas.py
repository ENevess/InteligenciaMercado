"""
🏦 Crédito Total para Pessoas Jurídicas (Empresas)
📅 Periodicidade: Mensal
🔢 Código SGS: 20616
"""

"""
Script para coletar a série de crédito total para empresas via API do Banco Central.
"""

from buildrate.utils.sgs_downloader import baixar_serie_sgs

if __name__ == "__main__":
    baixar_serie_sgs(
        codigo_sgs=20616,  # Código SGS para crédito PJ
        nome_serie="Crédito PJ",
        salvar_em="data/credit/credito_empresas.csv",
        inicio="01/01/2010"
    )
