import subprocess
import sys

# Lista de scripts a executar
scripts = [
    "buildrate.collection.collect_agropecuaria",
    "buildrate.collection.collect_consumo",
    #"buildrate.collection.collect_exportacoes",
    "buildrate.collection.collect_ibcbr",
    "buildrate.collection.collect_PIB",
    "buildrate.collection.collect_producao_industrial",
    "buildrate.collection.collect_ipca",
    "buildrate.collection.collect_igpm",
    "buildrate.collection.collect_selic",
    "buildrate.collection.collect_cdi",
    "buildrate.collection.collect_usd_brl",
    "buildrate.collection.collect_eur_brl",
    "buildrate.collection.collect_credito_empresas",
    "buildrate.collection.collect_brent",
    "buildrate.collection.collect_free_ontl",
    "buildrate.collection.collect_unemployment_pnadc_ipea",
]

def executar_todos():
    print("Iniciando execução dos scripts...\n")
    for script in scripts:
        print(f"Executando: {script}")
        resultado = subprocess.run(
            [sys.executable, "-m", script]
        )
        if resultado.returncode == 0:
            print("  -> Sucesso\n")
        else:
            print("  -> Erro\n")

if __name__ == "__main__":
    executar_todos()
