
# interface/streamlit_app.py

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from models.simulation.modelo_predicao import simular_cenario, gerar_comentario

# ⚠️ Precisa ser o primeiro comando
st.set_page_config(page_title="Inteligência de Mercado", layout="wide")

# Traduções multilíngue
TEXTOS = {
    "Português": {
        "titulo": "📊 Inteligência de Mercado",
        "menu_simulador": "🔧 Simulador de Cenário",
        "menu_correlacao": "📈 Mapa de Correlações",
        "variavel_label": "🔁 Qual variável você deseja prever?",
        "definir_variaveis": "### 📥 Defina os valores simulados para as variáveis abaixo:",
        "analisar": "🔍 Analisar cenário",
        "interpretacao": "🧠 Interpretação automática:",
        "grafico": "📈 Tendência esperada:",
        "correlacao": "📎 Correlação com a variável prevista:",
        "erro_correlacao": "Erro ao carregar correlações.",
        "explicacao": (
            "A matriz de correlação mostra o grau de associação entre os indicadores econômicos.\n\n"
            "Valores próximos de **1** indicam correlação positiva forte (ambos sobem juntos).\n\n"
            "Valores próximos de **-1** indicam correlação negativa forte (um sobe, o outro cai).\n\n"
            "Valores próximos de **0** indicam ausência de relação linear significativa."
        )
    },
    "English": {
        "titulo": "📊 Market Intelligence",
        "menu_simulador": "🔧 Scenario Simulator",
        "menu_correlacao": "📈 Correlation Map",
        "variavel_label": "🔁 Which variable do you want to predict?",
        "definir_variaveis": "### 📥 Set the simulated values for the variables below:",
        "analisar": "🔍 Analyze scenario",
        "interpretacao": "🧠 Automatic interpretation:",
        "grafico": "📈 Expected trend:",
        "correlacao": "📎 Correlation with the predicted variable:",
        "erro_correlacao": "Error loading correlation data.",
        "explicacao": (
            "The correlation matrix shows the strength of the relationship between economic indicators.\n\n"
            "Values close to **1** indicate strong positive correlation (both rise together).\n\n"
            "Values close to **-1** indicate strong negative correlation (one rises while the other falls).\n\n"
            "Values near **0** suggest little to no linear relationship."
        )
    }
}

# Idioma
idioma = st.sidebar.selectbox("🌐 Idioma / Language", ["Português", "English"])
txt = TEXTOS[idioma]

# Menu de abas
aba = st.sidebar.radio("📌 Menu", [txt["menu_simulador"], txt["menu_correlacao"], "📌 Visão Geral do Projeto"])

st.title(txt["titulo"])

if aba == txt["menu_simulador"]:
    # Aba do simulador
    target = st.selectbox(txt["variavel_label"], ["EURO", "DOLAR", "SELIC", "DIESEL"])

    variaveis = ["DIESEL", "SELIC", "DOLAR", "EURO"]
    inputs = {}

    st.markdown(txt["definir_variaveis"])
    for var in variaveis:
        if var != target:
            default = 5.0 if var in ["DIESEL", "DOLAR", "EURO"] else 10.0
            step = 0.1 if var in ["DIESEL", "DOLAR", "EURO"] else 0.25
            inputs[var] = st.number_input(f"{var}", min_value=0.0, max_value=100.0, value=default, step=step)

    if st.button(txt["analisar"]):
        resultado = simular_cenario(inputs, target)
        comentario = gerar_comentario(target, resultado, idioma)

        st.subheader(txt["interpretacao"])
        st.write(comentario)

        st.subheader(txt["grafico"])
        fig, ax = plt.subplots()
        ax.plot(resultado["meses"], resultado["valores"], label=target, linewidth=2)
        ax.set_xlabel("Meses" if idioma == "Português" else "Months")
        ax.set_ylabel(target)
        ax.set_title(f"Projeção para {target}" if idioma == "Português" else f"Projection for {target}")
        ax.grid(True)
        ax.legend()
        st.pyplot(fig)

        st.subheader(txt["correlacao"])
        try:
            cor_df = pd.read_csv("models/simulation/correlacoes.csv", index_col=0)
            cor_alvo = cor_df[target].drop(target)
            for var, valor in cor_alvo.items():
                emoji = "🔥" if abs(valor) > 0.7 else "⚠️" if abs(valor) > 0.4 else "💤"
                st.write(f"- {var}: {valor:.2f} {emoji}")
        except Exception as e:
            st.error(txt["erro_correlacao"])
            st.text(str(e))

elif aba == txt["menu_correlacao"]:
    st.subheader(txt["menu_correlacao"])
    st.markdown(txt["explicacao"])

    # Carregar dados da correlação
    arquivos = {
        "EURO": ("data/exchange_rates/eur_brl.csv", None),
        "DOLAR": ("data/exchange_rates/usd_brl.csv", None),
        "SELIC": ("data/interest_rates/selic.csv", None),
        "DIESEL": ("data/transport/diesel_anp_consolidado.csv", {"data": "DATA FINAL", "valor": "PREÇO MÉDIO REVENDA"}),
        "PIB": ("data/macro/pib.csv", None),
        "IBC_BR": ("data/macro/ibcbr.csv", None),
        "DESEMPREGO": ("data/macro/unemployment_rate_pnadc_ipea.csv", {"data": "data", "valor": "taxa_desemprego"}),
        "CREDITO EMPRESAS": ("data/credit/credito_empresas.csv", None),
        "IPCA": ("data/macro/ipca.csv", None),
        "IGPM": ("data/macro/igpm.csv", None),
        "PROD.IND": ("data/macro/producao_industrial.csv", None)
    }

    @st.cache_data
    def carregar_dados():
        df_final = pd.DataFrame()
        for nome, (caminho, colunas) in arquivos.items():
            try:
                df = pd.read_csv(caminho, sep=";" if "diesel" in caminho else ",")
                if colunas:
                    col_data = colunas["data"]
                    col_valor = colunas["valor"]
                else:
                    col_data = [col for col in df.columns if col.lower() in ["data", "date"]][0]
                    col_valor = [col for col in df.columns if col.lower() in ["valor", "value"]][0]
                df = df.rename(columns={col_data: "DATE", col_valor: nome})
                df["DATE"] = pd.to_datetime(df["DATE"], errors="coerce")
                df = df[["DATE", nome]].dropna()
                df_final = df if df_final.empty else pd.merge(df_final, df, on="DATE", how="outer")
            except Exception as e:
                st.warning(f"Erro ao carregar {nome}: {e}")
        df_final = df_final.dropna().sort_values("DATE").set_index("DATE")
        return df_final

    df = carregar_dados()

    if df.empty:
        st.error("❌ Nenhum dado encontrado.")
        st.stop()

    min_date, max_date = df.index.min(), df.index.max()
    range_values = st.slider(
        "Selecione o período de análise:",
        min_value=min_date.to_pydatetime(),
        max_value=max_date.to_pydatetime(),
        value=(min_date.to_pydatetime(), max_date.to_pydatetime()),
        format="YYYY-MM"
    )

    df_periodo = df.loc[range_values[0]:range_values[1]]
    cor = df_periodo.corr()

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(cor, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5, ax=ax)
    st.pyplot(fig)

elif aba == "📌 Visão Geral do Projeto":
    st.title("📌 Visão Geral do Projeto")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Fontes já integradas e entregas realizadas")

        st.markdown("### **Fontes de Dados Integradas**")
        st.markdown("""
        - **Banco Central do Brasil (BCB)**  
          - Câmbio: USD/BRL e EUR/BRL  
          - Selic: Taxa de juros básica  
          - Crédito para empresas (SGS 20616)  
        - **IPEA / IBGE (via ipeadatapy)**  
          - Taxa de desemprego (PNAD Contínua ajustada)  
        - **ANP - Agência Nacional do Petróleo**  
          - Preço do diesel consolidado (2004–2025)  
        - **ONTL - Observatório Nacional de Transporte e Logística**  
          - Preço médio do frete em R$/TKU (modal rodoviário)  
        - **Investing.com**  
          - Preço do petróleo Brent (via WebScraping)
        """)

        st.markdown("### **Infraestrutura já implementada**")
        st.markdown("""
        - Organização modular por tema (exchange, macro, transport...)
        - Scripts de coleta com comentários padronizados
        - Runner centralizado com log rotativo
        - Interface visual com Streamlit
        - Matriz de correlação com explicação bilíngue
        - Modelo inicial de regressão linear
        """)

    with col2:
        st.subheader("🚀 Próximos Passos do Projeto")

        passos = [
            ("Criar aba de exploração histórica interativa", 5, 2, "🔍 Foco em analisar individualmente cada variável ao longo do tempo com filtros de período e visualização detalhada."),
            ("Substituir modelo de regressão linear por RandomForest/XGBoost", 5, 4, "Aumenta a robustez das previsões."),
            ("Adicionar novos indicadores econômicos", 4, 2, "Ampliar base com produção, consumo, PIB, etc."),
            ("Exportação dos resultados para PDF e XLS", 4, 3, "Facilita envio de relatórios e apresentações."),
            ("Criar input textual para simulação (NLP simplificado)", 4, 4, "Simulação via linguagem natural."),
            ("Implementar logs detalhados de execução no runner.py", 3, 1, "Rastreabilidade das coletas."),
            ("Criar sistema de versão dos dados (carimbo de coleta)", 3, 2, "Base para auditoria."),
            ("Adicionar dashboard comparativo entre variáveis", 4, 3, "📊 Foco em exibir múltiplas variáveis no mesmo gráfico para facilitar comparação e análise de correlações visuais."),
            ("Validar previsões com dados internos futuros (build rate real)", 5, 4, "Comprova valor preditivo."),
            ("Adicionar camada de alerta automático por indicador", 3, 3, "Notificações para desvios anormais."),
        ]

        for nome, impacto, complexidade, desc in passos:
            st.markdown(f"**• {nome}**  \n> {desc}  \n> 🔥 Impacto: {'⭐' * impacto}  \n> 🧩 Complexidade: {'⭐' * complexidade}\n")
