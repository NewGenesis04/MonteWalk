# NewsAPI Setup Instructions

## Getting Your API Key

1. Go to [newsapi.org](https://newsapi.org/)
2. Click "Get API Key" (top right)
3. Sign up for the **Free tier** (70,000 requests/month)
4. Copy your API key from the dashboard

## Configuring the Server

### Option 1: Environment Variable (Recommended)
```bash
export NEWSAPI_KEY="your_api_key_here"
```

### Option 2: Add to your shell profile
Add to `~/.zshrc` or `~/.bashrc`:
```bash
export NEWSAPI_KEY="your_api_key_here"
```

Then reload:
```bash
source ~/.zshrc
```

### Option 3: Inline (for testing)
```bash
NEWSAPI_KEY="your_key" uv run server.py
```

## Verifying It Works

Run the test script:
```bash
NEWSAPI_KEY="your_key" uv run python -c "from tools.news_intelligence import get_newsapi_articles; print(get_newsapi_articles('AAPL', 3))"
```

## What It Does

- **Primary News Source**: NewsAPI is now the first fallback when yfinance fails
- **Quality**: Much better coverage than GNews for financial news
- **Limits**: 70,000 requests/month on free tier (≈2,300/day)
- **Fallback Chain**: yfinance → NewsAPI → GNews

## Without API Key

The server will still work! It will skip NewsAPI and use GNews as the fallback.
