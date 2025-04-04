# Value at Risk (VaR) com Simulação de Monte Carlo - BBSE3

Este projeto calcula o Value at Risk (VaR) das ações da BB Seguridade (BBSE3) usando simulação de Monte Carlo.

### Parâmetros:
- Ticker: BBSE3.SA
- Período histórico: 2020–2024
- Horizonte de risco: 10 dias
- Confiança: 95% e 99%
- Simulações: 1000

O código usa `yfinance`, `pandas`, `numpy` e `matplotlib`.

### Resultado (exemplo):
- VaR 95% (10 dias): -X.XX%
- VaR 99% (10 dias): -Y.YY%

### Gráfico:
O gráfico gerado será salvo na pasta `plots/` como `histogram_var.png`.
