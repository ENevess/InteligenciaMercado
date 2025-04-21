
# models/simulation/modelo_predicao.py

import pandas as pd
import joblib
import os

MODEL_DIR = "models/simulation/"
VARIAVEIS = ["EURO", "DOLAR", "SELIC", "DIESEL"]

def simular_cenario(inputs: dict, target: str):
    """
    Gera previsão para a variável 'target' com base nas outras variáveis do dicionário de entrada.
    """
    target = target.upper()
    features = [v for v in VARIAVEIS if v != target]
    model_path = os.path.join(MODEL_DIR, f"modelo_regressao_{target.lower()}.joblib")

    model = joblib.load(model_path)

    # Repetir valores por 6 meses
    X_input = pd.DataFrame({f: [inputs[f]] * 6 for f in features})
    pred = model.predict(X_input)
    meses = pd.date_range(start="2025-05-01", periods=6, freq="M")

    return {"meses": meses, "valores": pred}
    
def gerar_comentario(target, resultado, idioma="Português"):
    ultima = resultado["valores"][-1]
    if idioma == "English":
        return f"Based on the simulated scenario, the estimated value for **{target}** is expected to reach **R$ {ultima:.2f}** in the coming months."
    else:
        return f"Com base no cenário simulado, o valor estimado para **{target}** tende a alcançar **R$ {ultima:.2f}** nos próximos meses."
