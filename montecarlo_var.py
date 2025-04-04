import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Parâmetros do projeto
ticker = 'BBSE3.SA'
start_date = '2020-01-01'
end_date = '2024-12-31'
confidence_level = 0.95
days = 10
n_simulations = 1000

# 1. Baixar dados
data = yf.download(ticker, start=start_date, end=end_date)['Adj Close']
returns = np.log(data / data.shift(1)).dropna()

# 2. Estimar média e volatilidade
mu = returns.mean()
sigma = returns.std()

# 3. Simular caminhos com Monte Carlo
last_price = data[-1]
simulations = np.zeros((days, n_simulations))

for i in range(n_simulations):
    prices = [last_price]
    for _ in range(days):
        shock = np.random.normal(loc=mu, scale=sigma)
        prices.append(prices[-1] * np.exp(shock))
    simulations[:, i] = prices[1:]

# 4. Calcular retornos finais e VaR
final_prices = simulations[-1, :]
final_returns = (final_prices - last_price) / last_price
VaR_95 = np.percentile(final_returns, (1 - confidence_level) * 100)
VaR_99 = np.percentile(final_returns, 1)

# 5. Resultados
print(f"VaR 95% em {days} dias: {VaR_95:.2%}")
print(f"VaR 99% em {days} dias: {VaR_99:.2%}")

# 6. Visualizar distribuição
plt.hist(final_returns, bins=50, alpha=0.7, color='skyblue')
plt.axvline(VaR_95, color='red', linestyle='dashed', linewidth=2, label='VaR 95%')
plt.axvline(VaR_99, color='orange', linestyle='dashed', linewidth=2, label='VaR 99%')
plt.title(f'Distribuição de Retornos Simulados ({ticker})')
plt.xlabel('Retorno')
plt.ylabel('Frequência')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('plots/histogram_var.png')
plt.show()
