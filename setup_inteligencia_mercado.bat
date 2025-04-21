
@echo off
echo ----------------------------------------
echo   INTELIGENCIA DE MERCADO - SETUP
echo ----------------------------------------

REM Criar ambiente virtual
echo Criando ambiente virtual...
python -m venv venv

REM Ativar ambiente virtual
echo Ativando ambiente virtual...
call venv\Scripts\activate

REM Instalar dependências
echo Instalando dependências do projeto...
pip install -r requirements.txt

REM Iniciar aplicação Streamlit
echo Iniciando a aplicação...
streamlit run interface\streamlit_app.py

pause
