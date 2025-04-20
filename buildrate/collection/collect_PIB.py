"""
📊 PIB Trimestral a preços constantes (dessazonalizado)
📅 Periodicidade: Trimestral
🔢 Código SGS: 4380
"""

from buildrate.utils.sgs_downloader import baixar_serie_sgs

if __name__ == "__main__":
    baixar_serie_sgs(
        codigo_sgs=4380,
        nome_serie="PIB Trimestral",
        salvar_em="data/macro/pib.csv",
        inicio="01/01/2010"
    )
