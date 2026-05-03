@echo off
title Mercado Liquida - Servidor
color 0A
echo.
echo  ========================================
echo   MERCADO LIQUIDA - Iniciando servidor...
echo  ========================================
echo.

:: Verifica Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo  [ERRO] Python nao encontrado!
    echo  Baixe em: https://python.org/downloads
    echo  Marque "Add Python to PATH" na instalacao
    pause
    exit
)

:: Instala dependencias
echo  Instalando dependencias...
pip install -r requirements.txt -q

:: Inicia servidor
echo.
echo  ========================================
echo   Servidor rodando em:
echo   http://localhost:5000
echo  ========================================
echo.
echo  Pressione CTRL+C para parar
echo.
python app.py

pause
