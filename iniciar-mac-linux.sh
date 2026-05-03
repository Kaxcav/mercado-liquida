#!/bin/bash
echo ""
echo "=========================================="
echo "  Mercado Liquida - Iniciando servidor..."
echo "=========================================="
echo ""

# Instala dependencias
pip3 install flask requests --quiet 2>/dev/null || pip install flask requests --quiet

# Abre o navegador automaticamente
sleep 1.5 && open http://localhost:5000 2>/dev/null &
sleep 1.5 && xdg-open http://localhost:5000 2>/dev/null &

echo "Servidor em: http://localhost:5000"
echo "CTRL+C para parar"
echo ""
python3 app.py
