"""
📊 Exportações de Bens FOB (Free On Board)
📅 Periodicidade: Mensal
🔢 Código SGS: 22601
"""

from buildrate.utils.sgs_downloader import baixar_serie_sgs

if __name__ == "__main__":
    baixar_serie_sgs(
        codigo_sgs=22601,
        nome_serie="Exportações FOB",
        salvar_em="data/transport/exportacoes_fob.csv",
        inicio="01/01/2010"
    )
