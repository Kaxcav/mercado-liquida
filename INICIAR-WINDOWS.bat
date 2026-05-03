@echo off
title Mercado Liquida - Servidor
color 0A
echo.
echo  ==========================================
echo    Mercado Liquida - Iniciando servidor...
echo  ==========================================
echo.

:: Verifica se Python esta instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo  [ERRO] Python nao encontrado!
    echo  Baixe em: https://www.python.org/downloads/
    echo  Marque "Add Python to PATH" durante a instalacao.
    pause
    exit /b
)

:: Instala dependencias se necessario
echo  Verificando dependencias...
pip install flask requests --quiet --break-system-packages 2>nul || pip install flask requests --quiet

:: Inicia o servidor
echo.
echo  Servidor iniciado em: http://localhost:5000
echo  Pressione CTRL+C para parar.
echo.
start "" http://localhost:5000
python app.py
pause
