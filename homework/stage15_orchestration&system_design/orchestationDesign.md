# Orchestration Plan: Momentum Trading Automation

## 1. Key Tasks & Dependencies

**Tasks**:
1. `fetch_data`: Ingest S&P 100 stock data from API  
2. `clean_data`: Handle missing values, validate schema  
3. `feature_engineering`: Compute momentum indicators (e.g., RSI, MACD)  
4. `signal_generation`: Identify buy/sell signals  
5. `backtest_strategy`: Evaluate signal performance historically  
6. `execute_trades`: Send live trade orders via C++ engine  
7. `log_metrics`: Store PnL, Sharpe, drawdown  
8. `report_generation`: Summarize performance & alerts  

**DAG Sketch**:
fetch_data → clean_data → feature_engineering → signal_generation → [backtest_strategy, execute_trades]
↘ log_metrics → report_generation

- Tasks 5 and 6 can run in parallel post-signal generation.  
- Reporting depends on logging metrics.

---

## 2. Task Details

| Task               | Inputs                    | Outputs                   | Idempotent | Logging                     | Checkpoint |
|--------------------|----------------------------|----------------------------|------------|-----------------------------|------------|
| fetch_data         | API credentials, ticker list| Raw JSON/CSV               | N          | `logs/fetch.log`            | `data/raw/`|
| clean_data         | `data/raw/`                | `data/cleaned/`            | Y          | `logs/clean.log`            | ✅         |
| feature_engineering| `data/cleaned/`            | `features/`                | Y          | `logs/feature.log`          | ✅         |
| signal_generation  | `features/`                | `signals/`                 | Y          | `logs/signal.log`           | ✅         |
| backtest_strategy  | `signals/`, historical data| `backtest_results/`        | Y          | `logs/backtest.log`         | ✅         |
| execute_trades     | `signals/`                 | Trade execution via C++    | N          | `logs/trade_exec.log`       | ❌ (live)  |
| log_metrics        | Trading data, signals      | `logs/metrics.csv`         | Y          | `logs/metrics.log`          | ✅         |
| report_generation  | `logs/metrics.csv`         | `reports/summary.md`       | Y          | `logs/report.log`           | ✅         |

---

## 3. Failure Points & Retry Policy

- **fetch_data**: Failure due to API limits → retry up to 3 times with exponential backoff.  
- **clean_data**: Fail on schema mismatch → log and raise alert, no retry.  
- **execute_trades**: No retry (live system); raise alert for manual override.  
- **report_generation**: Retry once on I/O error.  

---

## 4. Automation Plan

### Automate Now:
- `fetch_data`, `clean_data`, `feature_engineering`, `signal_generation`, `log_metrics`, `report_generation`  
  *Rationale:* Deterministic, idempotent, suitable for scheduled orchestration (e.g., cron, Airflow)

### Keep Manual (For Now):
- `execute_trades`: Directly impacts capital; requires oversight  
- `backtest_strategy`: Run periodically or manually when strategies are updated

---

## 5. Logging & Checkpoint Strategy

- **Logging**: Standardized logs per task, stored in `logs/` directory using Python’s `logging` module.  
- **Checkpoints**: Store intermediate data in structured directories (`data/`, `features/`, `signals/`) with timestamped subfolders for auditability and rollback.

