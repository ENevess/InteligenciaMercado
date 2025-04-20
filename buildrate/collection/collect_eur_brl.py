"""
📊 Cotação de Venda do Euro (EUR/BRL)
📅 Periodicidade: Diária
🔢 Código SGS: 21619
"""

"""
Script para coletar a série de câmbio EUR/BRL via API do Banco Central.
"""

from buildrate.utils.sgs_downloader import baixar_serie_sgs

if __name__ == "__main__":
    baixar_serie_sgs(
        codigo_sgs=21619,  # Código SGS para EUR/BRL (cotação de venda)
        nome_serie="EUR/BRL",
        salvar_em="data/exchange_rates/eur_brl.csv",
        inicio="01/01/2010"
    )
