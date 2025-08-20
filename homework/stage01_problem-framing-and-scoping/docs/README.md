# Momentum Trading Automation

## Project Scope
This project develops and evaluates a **momentum-based equity trading strategy** that systematically selects U.S. stocks with the strongest recent returns over a 1–3 month lookback period and holds them for a fixed duration such as one month. The system automates data ingestion from public market APIs, preprocesses data for corporate actions, engineers momentum and volatility features, runs historical backtests, and benchmarks results against the S&P 500. Success is measured using quantifiable metrics — including cumulative return, Sharpe ratio, maximum drawdown, and hit rate — to determine whether the strategy outperforms the benchmark and is viable for live deployment. An interactive dashboard presents results, enabling informed trading decisions.

The **primary stakeholders** are quantitative traders and portfolio managers seeking systematic, rules-based strategies, while **secondary users** include quant researchers, analysts, and students studying factor investing. The project outputs are both **predictive** (using past momentum to anticipate short-term outperformance) and **descriptive** (summarizing historical performance and risk characteristics), producing both actionable **metrics** and a reusable **artifact** in the form of a backtesting engine and deployable dashboard. **Assumptions** include the availability of accurate and complete historical market data via public APIs and the validity of the S&P 500 as a benchmark. **Constraints** include focusing on U.S. equities only, limiting computation to available local or cloud resources, and recognizing that historical performance does not guarantee similar real-world results.

## Project Goals
- Build an automated **data ingestion and preprocessing pipeline** for U.S. equities.
- Implement a **momentum-based trading strategy** with backtesting and evaluation.
- Provide an interactive **dashboard** to visualize strategy performance metrics.

## Lifecycle
1. **Problem Framing & Scoping**: Define momentum strategy and performance benchmarks.
2. **Data Ingestion**: Pull historical price data from public APIs (e.g., yFinance).
3. **Preprocessing & Feature Engineering**: Adjust for splits/dividends, calculate momentum, volatility.
4. **Backtesting & Evaluation**: Rank stocks, simulate trades, compute Sharpe ratio, drawdown, hit rate.
5. **Reporting & Dashboard**: Visualize cumulative returns, performance metrics, and strategy outputs.
6. **Automation & Orchestration**: Schedule daily/weekly pipeline runs with cron or workflow tools.

## Deliverables
- Reproducible **Python code** for data ingestion, preprocessing, and strategy backtesting.
- **Dashboard** for visualizing key metrics and portfolio performance.
- **Documentation** in `/docs/` including methodology, assumptions, and usage guide.
- **Data outputs** stored in `/data/` for reproducibility and analysis.