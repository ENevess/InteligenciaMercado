"""
📊 PIB do Setor Agropecuário - preços correntes
📅 Periodicidade: Trimestral
🔢 Código SGS: 4385
"""

from buildrate.utils.sgs_downloader import baixar_serie_sgs

if __name__ == "__main__":
    baixar_serie_sgs(
        codigo_sgs=4385,
        nome_serie="PIB Agropecuária",
        salvar_em="data/macro/agropecuaria.csv",
        inicio="01/01/2010"
    )
