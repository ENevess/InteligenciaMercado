"""
📊 Vendas no Varejo Ampliado (volume dessazonalizado)
📅 Periodicidade: Mensal
🔢 Código SGS: 4382
"""

from buildrate.utils.sgs_downloader import baixar_serie_sgs

if __name__ == "__main__":
    baixar_serie_sgs(
        codigo_sgs=4382,
        nome_serie="Varejo Ampliado (Consumo Interno)",
        salvar_em="data/macro/consumo_interno.csv",
        inicio="01/01/2010"
    )
