# 🛒 Mercado Liquida — Site Completo

## ▶️ Como testar (Windows)

1. Extraia o ZIP em qualquer pasta
2. Clique duas vezes em **INICIAR-WINDOWS.bat**
3. O navegador abre sozinho em http://localhost:5000
4. Pronto!

---

## ▶️ Como testar (Mac / Linux)

```bash
chmod +x iniciar-mac-linux.sh
./iniciar-mac-linux.sh
```

---

## 🔗 Páginas disponíveis

| Endereço                        | O que é                        |
|---------------------------------|-------------------------------|
| http://localhost:5000           | Página do produto             |
| http://localhost:5000/login     | Login / Cadastro              |
| http://localhost:5000/carrinho  | Carrinho de compras           |
| http://localhost:5000/checkout  | Formulário de checkout        |
| http://localhost:5000/admin/pedidos | Painel de pedidos (admin) |

---

## 💳 Gateway de Pagamento

Integrado com **InvctusPay** (link de teste).
O botão "Comprar agora" redireciona para:
```
https://go.invictuspay.app.br/m387smwrlf_mpzmtfsx5d
```

Para trocar para o link de produção, abra `app.py` e edite:
```python
INVICTUS_CHECKOUT_URL = "https://go.invictuspay.app.br/SEU_LINK_PRODUCAO"
```

---

## 🔒 Login com Google

Para ativar, configure no arquivo `app.py`:
```python
GOOGLE_CLIENT_ID     = "seu-client-id.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "seu-client-secret"
GOOGLE_REDIRECT_URI  = "http://localhost:5000/auth/google/callback"
```
