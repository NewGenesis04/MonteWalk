# Classic Quantitative Finance Papers Summary

## 1. The Pricing of Options and Corporate Liabilities (Black & Scholes, 1973)
*   **Core Idea**: Introduced the Black-Scholes model for pricing European options.
*   **Key Insight**: It is possible to create a risk-free hedge portfolio by continuously adjusting the position in the underlying stock and the option. This leads to a partial differential equation (Black-Scholes PDE) governing the option price.
*   **Impact**: Revolutionized derivatives trading and risk management. Provided a standard formula for valuing options based on stock price, strike price, time to maturity, risk-free rate, and volatility.

## 2. The Cross-Section of Expected Stock Returns (Fama & French, 1992)
*   **Core Idea**: The Capital Asset Pricing Model (CAPM) beta alone does not explain the cross-section of expected stock returns.
*   **Key Insight**: Two other variables—**Size** (Market Capitalization) and **Book-to-Market Equity**—capture much of the variation in average stock returns that beta misses.
    *   Small-cap stocks tend to outperform large-cap stocks (Size Effect).
    *   Value stocks (high book-to-market) tend to outperform growth stocks (low book-to-market) (Value Effect).
*   **Impact**: Led to the Fama-French Three-Factor Model, a cornerstone of modern asset pricing and factor investing.

## 3. Optimal Execution of Portfolio Transactions (Almgren & Chriss, 2000)
*   **Core Idea**: How to trade a large block of shares while minimizing the combination of volatility risk and transaction costs (market impact).
*   **Key Insight**: There is a trade-off between execution speed and cost.
    *   **Fast execution**: Minimizes risk (exposure to market volatility) but maximizes market impact cost (pushing the price against yourself).
    *   **Slow execution**: Minimizes market impact but maximizes risk (price might drift away).
*   **Impact**: Established the framework for "Arrival Price" algorithms and optimal execution strategies used by institutional traders.

## 4. A Five-Factor Asset Pricing Model (Fama & French, 2015)
*   **Core Idea**: Expanded the Three-Factor model to include two new factors: **Profitability** and **Investment**.
*   **Key Insight**:
    *   **Profitability**: Stocks with high operating profitability perform better.
    *   **Investment**: Stocks of companies with high total asset growth (aggressive investment) perform worse.
*   **Impact**: Refined the understanding of what drives stock returns, influencing "Smart Beta" strategies.
