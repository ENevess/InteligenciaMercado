"""
📊 Cotação de Venda do Dólar (USD/BRL)
📅 Periodicidade: Diária
🔢 Código SGS: 1
"""

"""
Script para coletar a série de câmbio USD/BRL via API do Banco Central.
"""

from buildrate.utils.sgs_downloader import baixar_serie_sgs

if __name__ == "__main__":
    baixar_serie_sgs(
        codigo_sgs=1,  # Código SGS para USD/BRL (cotação de venda)
        nome_serie="USD/BRL",
        salvar_em="data/exchange_rates/usd_brl.csv",
        inicio="01/01/2010"
    )
