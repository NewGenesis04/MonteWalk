# Codebase Audit Report

## 🔴 Critical Issues

### 1. **Duplicate Dependency in pyproject.toml**
**File**: `pyproject.toml`  
**Issue**: `pandas_ta` is listed twice in dependencies  
**Impact**: Build errors or confusion  
**Fix**: Remove duplicate entry

---

## 🟡 Medium Priority Issues

### 2. **Placeholder Implementations (Not Production-Ready)**

**File**: `tools/backtesting.py`
- `simulate_order_flow()` - Returns "Not implemented"
- `strategy_metrics()` - Returns "Not implemented"

**File**: `tools/risk_engine.py`
- `exposure_by_asset_class()` - Returns "Not implemented"

**File**: `tools/portfolio_optimizer.py`
- `rebalance()` - Only has placeholder logic

**Impact**: Tools are registered but non-functional. LLM will see error messages.  
**Recommendation**: Either implement these or remove them from tool registration.

---

### 3. **Missing Environment Variable Template**

**Missing File**: `.env.example`  
**Issue**: No template for users to configure API keys  
**Impact**: Users don't know what env vars are needed  
**Recommended Content**:
```env
# Optional: NewsAPI key for enhanced news coverage
# Get yours at https://newsapi.org/
NEWSAPI_KEY=

# Add other API keys here as needed
# ALPHA_VANTAGE_KEY=
# FRED_API_KEY=
```

---

### 4. **Minimal Test Coverage**

**File**: `tests/test_basic.py`  
**Issue**: Only 4 basic tests, no coverage for:
- News intelligence tools
- Crypto tools
- Portfolio optimization
- Technical analysis
- Watchlist management
- Risk validation

**Impact**: No safety net for regressions  
**Recommendation**: Add comprehensive test suite

---

### 5. **Missing Resource/Tool Documentation**

**Issue**: No centralized API documentation listing all 25 tools, 4 resources, and 2 prompts  
**Impact**: Users can't easily discover capabilities  
**Recommendation**: Create `API_REFERENCE.md`

---

## 🟢 Minor Issues

### 6. **Inconsistent Duplicate Import in server.py**

**File**: `server.py` Line 15-16  
**Issue**: `from tools.logger import log_action` appears twice  
**Fix**: Remove duplicate

---

### 7. **Risk Validation Only Checks Cash**

**File**: `tools/risk_engine.py` - `validate_trade()`  
**Issue**: Only validates against cash, not total equity (cash + positions)  
**Impact**: Allows oversized positions if you have illiquid holdings  
**Recommendation**: Calculate total portfolio value for percentage checks

---

### 8. **No Rate Limiting for External APIs**

**Issue**: No rate limiting on yfinance, NewsAPI, or CoinGecko calls  
**Impact**: Could hit API limits and get blocked  
**Recommendation**: Add caching and rate limiting (e.g., `ratelimit` library)

---

### 9. **Missing Data Validation on Tool Inputs**

**Example**: `place_order()` accepts `qty` as float, but doesn't validate:
- Positive number
- Maximum order size
- Symbol validity (until it hits yfinance)

**Impact**: Poor error messages for edge cases  
**Recommendation**: Add Pydantic models for input validation

---

### 10. **No Default Portfolio Initialization**

**File**: `tools/execution.py`  
**Issue**: If `data/portfolio.json` doesn't exist, it creates one on-the-fly  
**Concern**: Users might not realize they have a "mock" account  
**Recommendation**: Add explicit setup step or tutorial

---

## 📊 Summary Statistics

| Metric | Count |
|--------|-------|
| Total Tools Registered | 25 |
| Placeholder/Incomplete Tools | 4 |
| Resources | 4 |
| Prompts | 2 |
| Test Files | 1 |
| Test Coverage | ~20% (estimate) |
| External API Dependencies | 3 (yfinance, NewsAPI, CoinGecko) |

---

## 🎯 Recommended Priority Fixes

### Immediate (Next Session):
1. ✅ Remove duplicate `pandas_ta` from pyproject.toml
2. ✅ Remove duplicate import in server.py
3. ✅ Create `.env.example` file
4. ✅ Either implement or remove placeholder tools

### Short-term (This Week):
5. Create `API_REFERENCE.md` with all tools/resources/prompts
6. Improve risk validation to use total equity
7. Add comprehensive test suite

### Long-term (Nice to Have):
8. Add rate limiting and caching
9. Add Pydantic input validation
10. Create interactive onboarding tutorial

---

## ✅ What's Working Well

- **Core functionality is solid**: Market data, execution, risk, backtesting all work
- **Good separation of concerns**: Tools are modular
- **MCP integration is correct**: Resources and prompts properly registered
- **Documentation is comprehensive**: README, VSCODE_SETUP, NEWSAPI_SETUP are helpful
- **Error handling exists**: Most functions have try/except blocks
- **Type hints are present**: Most functions use type annotations
