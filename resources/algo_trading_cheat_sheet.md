# Algorithmic Trading Cheat Sheet

## 1. Common Strategies

### Mean Reversion
*   **Concept**: Asset prices tend to revert to their historical mean over time.
*   **Key Indicators**: Bollinger Bands, RSI, Moving Averages.
*   **Entry**: Buy when price is significantly below the mean (oversold).
*   **Exit**: Sell when price returns to the mean or becomes overbought.
*   **Risk**: Price may trend away from the mean for extended periods (momentum).

### Momentum / Trend Following
*   **Concept**: Assets that have performed well in the past will continue to perform well.
*   **Key Indicators**: Moving Average Crossovers (e.g., Golden Cross), MACD, ADX.
*   **Entry**: Buy when a positive trend is established (e.g., price > 200-day MA).
*   **Exit**: Sell when the trend reverses.
*   **Risk**: Whipsaws in sideways markets; late entries/exits.

### Statistical Arbitrage (Pairs Trading)
*   **Concept**: Exploit pricing inefficiencies between two correlated assets.
*   **Logic**: If Asset A and Asset B are historically correlated but diverge, short the outperforming asset and long the underperforming one.
*   **Formula**: Spread = Price(A) - HedgeRatio * Price(B).
*   **Entry**: When Z-score of the Spread > 2 (or < -2).
*   **Exit**: When Z-score returns to 0.

## 2. Key Definitions

*   **Alpha**: The excess return of an investment relative to the return of a benchmark index.
*   **Beta**: A measure of the volatility (or systematic risk) of a security or portfolio in comparison to the market as a whole.
*   **Sharpe Ratio**: (Return of Portfolio - Risk-Free Rate) / Standard Deviation of Portfolio Excess Return. Measures risk-adjusted return.
*   **Drawdown**: The peak-to-trough decline during a specific recorded period of an investment.
*   **Slippage**: The difference between the expected price of a trade and the price at which the trade is executed.
*   **Market Impact**: The effect that a market participant has when it buys or sells an asset.

## 3. Essential Formulas

### Simple Moving Average (SMA)
$$ SMA_n = \frac{P_1 + P_2 + ... + P_n}{n} $$

### Exponential Moving Average (EMA)
$$ EMA_t = P_t \times k + EMA_{t-1} \times (1-k) $$
where $k = \frac{2}{n+1}$

### Relative Strength Index (RSI)
$$ RSI = 100 - \frac{100}{1 + RS} $$
where $RS = \frac{\text{Average Gain}}{\text{Average Loss}}$

### Bollinger Bands
*   Middle Band = 20-day SMA
*   Upper Band = 20-day SMA + (2 * 20-day Standard Deviation)
*   Lower Band = 20-day SMA - (2 * 20-day Standard Deviation)
