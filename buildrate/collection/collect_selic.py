"""
📊 Taxa Selic Meta (mensal)
📅 Periodicidade: Mensal
🔢 Código SGS: 1178
"""

"""
Script para coletar a série da Selic Meta mensal via API do Banco Central.
"""

from buildrate.utils.sgs_downloader import baixar_serie_sgs

if __name__ == "__main__":
    baixar_serie_sgs(
        codigo_sgs=1178,  # Código SGS para Selic Meta
        nome_serie="Selic Meta",
        salvar_em="data/interest_rates/selic.csv",
        inicio="01/01/2010"
    )
