# Alpaca Paper Trading Setup Guide

This guide will help you set up Alpaca paper trading for MonteWalk.

## What is Alpaca Paper Trading?

Alpaca provides a **free paper trading environment** that mirrors real market conditions:
- ✅ $100,000 virtual starting capital
- ✅ Real-time market data
- ✅ Live order execution (simulated)
- ✅ Professional-grade API
- ✅ No credit card required

## Step 1: Create Alpaca Account

1. Visit [alpaca.markets](https://alpaca.markets)
2. Click **"Sign Up"** (top right)
3. Fill out the registration form
4. Verify your email address

> **Note**: You don't need to fund the account or provide payment information for paper trading.

## Step 2: Generate Paper Trading API Keys

1. Log in to your Alpaca account
2. Go to the **Dashboard**: https://app.alpaca.markets/paper/dashboard/overview
3. Click on **"API Keys"** in the left sidebar (under "Your API Keys")
4. Click **"Generate New Key"**
5. Give it a name (e.g., "MonteWalk Paper Trading")
6. Click **"Generate"**
7. **IMPORTANT**: Copy both keys immediately:
   - `API Key ID` (starts with `PK...`)
   - `Secret Key` (longer, alphanumeric)

> ⚠️ **Warning**: The secret key is only shown once. Store it securely!

## Step 3: Configure MonteWalk

1. Navigate to your MonteWalk directory:
   ```bash
   cd /home/mario/MonteWalk
   ```

2. Create a `.env` file (if it doesn't exist):
   ```bash
   cp .env.example .env
   ```

3. Edit the `.env` file and add your Alpaca credentials:
   ```bash
   ALPACA_API_KEY=PK*****************************
   ALPACA_SECRET_KEY=*********************************
   ```

4. Save the file

> 🔒 **Security**: Never commit your `.env` file to git. It's already in `.gitignore`.

## Step 4: Install Dependencies

Make sure the Alpaca SDK is installed:

```bash
# Using uv (recommended)
uv pip install alpaca-py

# Or using pip
pip install alpaca-py
```

## Step 5: Test Connection

Run the connection test script:

```bash
python test_alpaca_connection.py
```

Expected output:
```
✅ Alpaca Connection Successful!
📊 Account Balance: $100,000.00
📈 Equity: $100,000.00
💵 Buying Power: $400,000.00
📋 Open Positions: 0
```

## Step 6: Start MCP Server

```bash
python server.py
```

If successful, you'll see:
```
INFO - Alpaca broker initialized (Paper Trading Mode)
INFO - Starting MCP server...
```

## Using Alpaca in MonteWalk

### Place an Order
```python
place_order("AAPL", "buy", 10)
# ✅ Market Order Submitted: BUY 10 AAPL
```

### Check Portfolio
```python
get_positions()
# Returns: {'cash': 98500.0, 'equity': 100000.0, 'positions': {'AAPL': 10}}
```

### View Order History
```python
get_order_history()
# Shows all your orders with status
```

### Get Account Info
```python
get_account_info()
# Detailed account information with buying power
```

### Close All Positions
```python
flatten()
# ✅ Flattened 1 positions: AAPL: 10 shares (filled)
```

## Monitoring Your Trades

View your paper trading activity in the Alpaca dashboard:
- **Dashboard**: https://app.alpaca.markets/paper/dashboard/overview
- **Portfolio**: See your positions, P/L, and equity graph
- **Orders**: View order history and filled orders
- **Account**: Check buying power and day trade count

## Troubleshooting

### Error: "Alpaca broker not initialized"
- Make sure your `.env` file has valid `ALPACA_API_KEY` and `ALPACA_SECRET_KEY`
- Restart the MCP server after editing `.env`

### Error: "Failed to get account"
- Verify your API keys are correct
- Make sure you're using **paper trading** keys (not live trading keys)
- Check that the keys haven't been revoked in the Alpaca dashboard

### Error: "Insufficient buying power"
- Paper trading accounts have margin enabled ($400k buying power with $100k equity)
- Large orders may still exceed buying power limits

### Market Hours
- Alpaca paper trading follows real market hours (9:30 AM - 4:00 PM ET)
- Orders placed outside market hours will be queued until market opens
- Use extended hours trading if needed (not enabled by default)

## API Rate Limits

Alpaca paper trading has generous rate limits:
- **200 requests/minute** for most endpoints
- **Orders**: 200/minute
- **Market Data**: No hard limit for paper trading

## Next Steps

- ✅ Test placing your first order
- ✅ Run a backtest and execute the strategy
- ✅ Use the risk analysis tools with your Alpaca portfolio
- ✅ Set up prompts for automated trading workflows

## Need Help?

- **Alpaca Docs**: https://alpaca.markets/docs/
- **MonteWalk Issues**: Check the GitHub repository
- **API Reference**: See `API_REFERENCE.md` for all available tools

---

**Happy Paper Trading! 📈**
