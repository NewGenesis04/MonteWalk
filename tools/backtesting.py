import pandas as pd
import pandas_ta as ta
import yfinance as yf
import numpy as np
from typing import Dict, Any, List, Tuple

def _fetch_data(symbol: str, start: str, end: str):
    return yf.download(symbol, start=start, end=end, progress=False)

def run_backtest(symbol: str, fast_ma: int, slow_ma: int, start_date: str = "2020-01-01", end_date: str = "2023-12-31") -> str:
    """
    Backtests a Moving Average Crossover strategy.
    """
    try:
        logger.info(f"Starting backtest for {symbol} (Fast: {fast_ma}, Slow: {slow_ma}) from {start_date} to {end_date}")
        data = get_price(symbol, interval="1d", period="max")
        df = pd.DataFrame(json.loads(data))
        
        if df.empty:
            logger.warning(f"Backtest failed: No data for {symbol}")
            return f"No data found for {symbol}"
            
        # Filter by date
        df['Date'] = pd.to_datetime(df['Date'], utc=True)
        mask = (df['Date'] >= pd.to_datetime(start_date, utc=True)) & (df['Date'] <= pd.to_datetime(end_date, utc=True))
        df = df.loc[mask].copy()
        
        if df.empty:
            logger.warning(f"Backtest failed: No data in date range for {symbol}")
            return "No data in specified date range."
            
        # Strategy Logic
        df['Fast_MA'] = ta.sma(df['Close'], length=fast_ma)
        df['Slow_MA'] = ta.sma(df['Close'], length=slow_ma)
        
        # Signals
        df['Signal'] = 0
        df.loc[df['Fast_MA'] > df['Slow_MA'], 'Signal'] = 1
        df['Position'] = df['Signal'].diff()
        
        # Calculate Returns
        df['Market_Return'] = df['Close'].pct_change()
        df['Strategy_Return'] = df['Market_Return'] * df['Signal'].shift(1)
        
        # Metrics
        total_return = (1 + df['Strategy_Return']).prod() - 1
        buy_hold_return = (1 + df['Market_Return']).prod() - 1
        
        # Max Drawdown
        cum_ret = (1 + df['Strategy_Return']).cumprod()
        peak = cum_ret.expanding(min_periods=1).max()
        dd = (cum_ret / peak) - 1
        max_dd = dd.min()
        
        # Sharpe Ratio (assuming 0% risk free for simplicity or use config)
        sharpe = df['Strategy_Return'].mean() / df['Strategy_Return'].std() * np.sqrt(252)
        
        result = (
            f"Backtest Results for {symbol} ({start_date} to {end_date}):\n"
            f"Strategy: MA Crossover ({fast_ma}/{slow_ma})\n"
            f"------------------------------------------------\n"
            f"Total Return: {total_return:.2%}\n"
            f"Buy & Hold Return: {buy_hold_return:.2%}\n"
            f"Sharpe Ratio: {sharpe:.2f}\n"
            f"Max Drawdown: {max_dd:.2%}"
        )
        logger.info(f"Backtest completed for {symbol}. Return: {total_return:.2%}")
        return result

    except Exception as e:
        logger.error(f"Backtest failed for {symbol}: {e}", exc_info=True)
        return f"Error running backtest: {str(e)}"

def walk_forward_analysis(symbol: str, start_date: str = "2020-01-01", end_date: str = "2023-12-31", train_months: int = 12, test_months: int = 3) -> str:
    """
    Performs Walk Forward Analysis on MA Crossover.
    Optimizes (Fast, Slow) on Train, tests on Test.
    """
    df = _fetch_data(symbol, start_date, end_date)
    if df.empty:
        return "No data found."
    
    close = df['Close']
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]
        
    # Generate windows
    # Simplified: Iterate by index assuming daily data
    # 21 days/month
    train_len = train_months * 21
    test_len = test_months * 21
    step = test_len
    
    results = []
    
    # Parameter Grid
    fast_params = [10, 20, 50]
    slow_params = [50, 100, 200]
    
    current_idx = 0
    while current_idx + train_len + test_len < len(df):
        train_data = close.iloc[current_idx : current_idx + train_len]
        test_data = close.iloc[current_idx + train_len : current_idx + train_len + test_len]
        
        # Optimize on Train
        best_perf = -np.inf
        best_params = (0, 0)
        
        for f in fast_params:
            for s in slow_params:
                if f >= s: continue
                # Vectorized backtest on train
                fast_ma = train_data.rolling(window=f).mean()
                slow_ma = train_data.rolling(window=s).mean()
                signal = (fast_ma > slow_ma).astype(int).shift(1)
                ret = train_data.pct_change() * signal
                perf = ret.sum() # Simple sum of returns
                
                if perf > best_perf:
                    best_perf = perf
                    best_params = (f, s)
        
        # Test on Test Data
        f, s = best_params
        fast_ma_test = test_data.rolling(window=f).mean()
        slow_ma_test = test_data.rolling(window=s).mean()
        signal_test = (fast_ma_test > slow_ma_test).astype(int).shift(1)
        ret_test = test_data.pct_change() * signal_test
        test_perf = ret_test.sum()
        
        results.append({
            "Period": f"{test_data.index[0].date()} to {test_data.index[-1].date()}",
            "Best Params": best_params,
            "Test Return": test_perf
        })
        
        current_idx += step
        
    # Format Output
    output = ["Walk Forward Analysis Results:"]
    total_ret = 0
    for r in results:
        output.append(f"[{r['Period']}] Params: {r['Best Params']}, Return: {r['Test Return']:.2%}")
        total_ret += r['Test Return']
        
    output.append(f"Total Walk Forward Return: {total_ret:.2%}")
    return "\n".join(output)
