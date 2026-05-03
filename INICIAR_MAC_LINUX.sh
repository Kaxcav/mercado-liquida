#!/bin/bash
echo ""
echo "========================================"
echo "  MERCADO LIQUIDA - Iniciando servidor"
echo "========================================"
echo ""

# Instala dependencias
pip3 install -r requirements.txt -q 2>/dev/null || pip install -r requirements.txt -q

echo ""
echo "========================================"
echo "  Servidor rodando em:"
echo "  http://localhost:5000"
echo "========================================"
echo ""

python3 app.py 2>/dev/null || python app.py
