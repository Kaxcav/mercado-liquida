<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>{{ produto.nome }} – Mercado Liquida</title>
  <link href="https://fonts.googleapis.com/css2?family=Lexend:wght@400;500;600;700&display=swap" rel="stylesheet"/>
  <style>
    *{box-sizing:border-box;margin:0;padding:0}
    body{font-family:'Lexend',sans-serif;background:#f0f0f0;color:#1a1a1a}
    .nav{background:#1a2744;color:#fff;padding:0 2rem;height:56px;display:flex;align-items:center;gap:1rem}
    .nav-logo{font-size:17px;font-weight:600;display:flex;align-items:center;gap:8px}
    .nav-logo-icon{width:28px;height:28px;background:#fff;border-radius:6px;display:flex;align-items:center;justify-content:center}
    .subnav{background:#1e3060;display:flex;padding:0 2rem;overflow-x:auto}
    .subnav a{color:#d0d8f0;text-decoration:none;font-size:13px;padding:10px 14px;white-space:nowrap;border-bottom:2px solid transparent}
    .subnav a:hover{color:#fff;border-bottom-color:#fff}
    .breadcrumb{padding:12px 2rem;font-size:12px;color:#666}
    .wrap{max-width:1100px;margin:0 auto;padding:0 2rem 3rem}
    .product{display:grid;grid-template-columns:1fr 380px;gap:1.5rem}
    @media(max-width:720px){.product{grid-template-columns:1fr}}

    .gallery{background:#fff;border-radius:10px;padding:1.5rem}
    .main-img{aspect-ratio:1;display:flex;align-items:center;justify-content:center;background:#f8f8f8;border-radius:8px;margin-bottom:1rem;font-size:100px}
    .thumbs{display:flex;gap:8px;justify-content:center}
    .thumb{width:64px;height:64px;border-radius:6px;border:2px solid #ddd;cursor:pointer;background:#f8f8f8;display:flex;align-items:center;justify-content:center;font-size:28px;transition:border-color .2s}
    .thumb.active,.thumb:hover{border-color:#1a2744}
    .share{display:flex;align-items:center;gap:8px;margin-top:1rem;font-size:13px;color:#666;justify-content:center}

    .info{background:#fff;border-radius:10px;padding:1.5rem;position:sticky;top:1rem}
    .badges{display:flex;gap:8px;margin-bottom:10px;align-items:center}
    .badge-new{background:#22c55e;color:#fff;font-size:11px;font-weight:700;padding:3px 10px;border-radius:4px}
    .badge-sold{font-size:12px;color:#666}
    h1{font-size:19px;font-weight:600;line-height:1.35;margin-bottom:10px}
    .stars{display:flex;gap:5px;align-items:center;margin-bottom:14px}
    .star{color:#f59e0b;font-size:15px}
    .reviews{font-size:13px;color:#1a2744;text-decoration:underline;cursor:pointer}
    .price-old{font-size:13px;color:#999;text-decoration:line-through;margin-bottom:4px}
    .price-row{display:flex;align-items:center;gap:10px;margin-bottom:4px}
    .price{font-size:28px;font-weight:700}
    .discount{background:#22c55e;color:#fff;font-size:12px;font-weight:700;padding:3px 8px;border-radius:4px}
    .installment{font-size:13px;color:#555;margin-bottom:14px}
    .installment strong{color:#1a2744}
    .shipping{background:#f0fdf4;border:1px solid #bbf7d0;border-radius:8px;padding:10px 14px;display:flex;align-items:center;gap:10px;margin-bottom:14px}
    .shipping-text strong{font-size:13px;color:#166534;display:block;font-weight:600}
    .shipping-text span{font-size:12px;color:#15803d}
    .qty-label{font-size:13px;color:#555;margin-bottom:7px}
    .qty{display:flex;align-items:center;gap:10px;margin-bottom:14px}
    .qty-btn{width:32px;height:32px;border:1.5px solid #ccc;border-radius:6px;background:#fff;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:border-color .2s}
    .qty-btn:hover{border-color:#1a2744}
    .qty-val{font-size:15px;font-weight:600;min-width:20px;text-align:center}
    .qty-stock{font-size:12px;color:#888}
    .btn-buy{width:100%;height:48px;background:#1a2744;color:#fff;border:none;border-radius:8px;font-size:15px;font-weight:700;cursor:pointer;margin-bottom:10px;font-family:'Lexend',sans-serif;transition:background .2s}
    .btn-buy:hover{background:#243560}
    .btn-cart{width:100%;height:48px;background:#fff;color:#1a2744;border:1.5px solid #1a2744;border-radius:8px;font-size:15px;font-weight:500;cursor:pointer;margin-bottom:14px;font-family:'Lexend',sans-serif}
    .btn-cart:hover{background:#f0f4ff}
    .guarantees{display:flex;flex-direction:column;gap:9px}
    .guarantee{display:flex;align-items:flex-start;gap:8px;font-size:12px;color:#444;line-height:1.4}

    .desc{background:#fff;border-radius:10px;padding:1.5rem;margin-top:1.5rem}
    .desc h3{font-size:15px;font-weight:600;margin-bottom:10px}
    .desc p{font-size:14px;color:#444;line-height:1.7;margin-bottom:10px}
    .desc ul{padding-left:1.2rem;display:flex;flex-direction:column;gap:5px;list-style:disc}
    .desc li{font-size:14px;color:#444;line-height:1.6}

    footer{text-align:center;padding:2rem;font-size:12px;color:#888;border-top:1px solid #ddd;margin-top:2rem}
    footer p+p{margin-top:4px}
  </style>
</head>
<body>

<nav class="nav">
  <div class="nav-logo">
    <div class="nav-logo-icon">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#1a2744" stroke-width="2.5">
        <path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4z"/>
        <line x1="3" y1="6" x2="21" y2="6"/>
        <path d="M16 10a4 4 0 01-8 0"/>
      </svg>
    </div>
    Mercado Liquida
  </div>
</nav>

<div class="subnav">
  <a href="#">Ofertas do dia</a><a href="#">Eletrônicos</a><a href="#">Moda</a>
  <a href="#">Casa</a><a href="#">Esportes</a><a href="#">Mais vendidos</a>
</div>

<div class="breadcrumb">Início › Produtos › {{ produto.nome[:40] }}...</div>

<div class="wrap">
  <div class="product">
    <div>
      <div class="gallery">
        <div class="main-img">🍳</div>
        <div class="thumbs">
          <div class="thumb active">🍳</div>
          <div class="thumb">🥘</div>
          <div class="thumb">🫕</div>
          <div class="thumb">🥗</div>
        </div>
        <div class="share">
          <span>Compartilhar:</span>
          <span style="cursor:pointer;font-size:18px">📘</span>
          <span style="cursor:pointer;font-size:18px">🐦</span>
          <span style="cursor:pointer;font-size:18px">💬</span>
        </div>
      </div>
      <div class="desc">
        <h3>Descrição do Produto</h3>
        <p>ESSENCIAIS E PERFEITAS NA COZINHA! O Jogo De Panelas Antiaderente Paris de Tramontina é a adição ideal para uma cozinha funcional e cheia de estilo! Contém 10 peças na cor Vermelha, desenvolvidas com revestimento antiaderente de alta qualidade.</p>
        <ul>
          <li>Produto 100% original</li>
          <li>Garantia de 12 meses</li>
          <li>Envio imediato após confirmação do pagamento</li>
          <li>Embalagem segura e discreta</li>
        </ul>
      </div>
    </div>

    <div class="info">
      <div class="badges">
        <span class="badge-new">Novo</span>
        <span class="badge-sold">| +500 vendidos</span>
      </div>
      <h1>{{ produto.nome }}</h1>
      <div class="stars">
        <span class="star">★</span><span class="star">★</span><span class="star">★</span>
        <span class="star">★</span><span class="star" style="opacity:.4">★</span>
        <span class="reviews">(127 avaliações)</span>
      </div>
      <p class="price-old">R$ {{ "%.2f"|format(produto.preco_antigo) }}</p>
      <div class="price-row">
        <span class="price">R$ {{ "%.2f"|format(produto.preco) }}</span>
        <span class="discount">{{ produto.desconto }}</span>
      </div>
      <p class="installment">em até <strong>{{ produto.parcelas }}x de R$ {{ "%.2f"|format(produto.parcela_valor) }}</strong> sem juros</p>
      <div class="shipping">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2.5">
          <rect x="1" y="3" width="15" height="13" rx="1"/>
          <path d="M16 8h4l3 3v5h-7V8z"/>
          <circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/>
        </svg>
        <div class="shipping-text">
          <strong>Frete Grátis</strong>
          <span>Receba em até 5 dias úteis</span>
        </div>
      </div>
      <p class="qty-label">Quantidade:</p>
      <div class="qty">
        <button class="qty-btn" onclick="changeQty(-1)">−</button>
        <span class="qty-val" id="qty">1</span>
        <button class="qty-btn" onclick="changeQty(1)">+</button>
        <span class="qty-stock">(+50 disponíveis)</span>
      </div>
      <button class="btn-buy" onclick="comprar()">Comprar agora</button>
      <button class="btn-cart">Adicionar ao carrinho</button>
      <div class="guarantees">
        <div class="guarantee">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          <span><strong>Compra Garantida:</strong> receba o produto ou devolvemos seu dinheiro</span>
        </div>
        <div class="guarantee">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#3b82f6" stroke-width="2"><path d="M1 4v6h6"/><path d="M23 20v-6h-6"/><path d="M20.49 9A9 9 0 005.64 5.64L1 10M23 14l-4.64 4.36A9 9 0 013.51 15"/></svg>
          <span><strong>Devolução grátis:</strong> 30 dias a partir do recebimento</span>
        </div>
        <div class="guarantee">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#a855f7" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg>
          <span><strong>Pagamento seguro:</strong> seus dados estão protegidos</span>
        </div>
      </div>
    </div>
  </div>
</div>

<footer>
  <p>© 2024 Mercado Liquida – Todos os direitos reservados</p>
  <p>CNPJ: 00.000.000/0001-00 | contato@megastore.com.br</p>
</footer>

<script>
  let qtd = 1;
  function changeQty(d){
    qtd = Math.max(1, Math.min(50, qtd + d));
    document.getElementById('qty').textContent = qtd;
  }
  function comprar(){
    window.location.href = '/checkout?qtd=' + qtd;
  }
</script>
</body>
</html>
