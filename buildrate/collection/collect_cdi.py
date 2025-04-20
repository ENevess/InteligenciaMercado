"""
📊 Taxa CDI (média diária)
📅 Periodicidade: Diária
🔢 Código SGS: 12
"""

"""
Script para coletar a série do CDI diário via API do Banco Central.
"""

from buildrate.utils.sgs_downloader import baixar_serie_sgs

if __name__ == "__main__":
    baixar_serie_sgs(
        codigo_sgs=12,  # CDI médio diário
        nome_serie="CDI Diário",
        salvar_em="data/interest_rates/cdi.csv",
        inicio="01/01/2010"
    )
