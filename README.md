````markdown
# 📊 Financial Dashboard Automation

This project automates downloading, processing, analyzing, and reporting of financial stock data using Python, Machine Learning, and FastAPI.

---

## ✨ Features

✅ Fetch financial data from Yahoo Finance (via `yfinance`)  
✅ Clean and process data (Pandas)  
✅ Calculate indicators (moving average, volatility)  
✅ Generate plots and HTML reports (Matplotlib)  
✅ Basic ML prediction (will the price go up/down tomorrow)  
✅ Expose REST API (via FastAPI) to fetch reports and predictions  
✅ Trigger manual analysis directly from a web interface  
✅ Fully configurable via `config.json`  
✅ Run anywhere with Docker

---

## 📦 Requirements

- Python 3.10+
- Libraries (see `requirements.txt`):
  - pandas
  - yfinance
  - matplotlib
  - scikit-learn
  - fastapi
  - uvicorn
  - schedule

---

## ⚙ How to Use (Locally)

1️⃣ Clone this repository:

```bash
git clone <your-repo-url>
cd financial-dashboard
```
````

2️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

3️⃣ Edit `config.json` to choose your stock ticker, period, and interval:

```json
{
  "ticker": "AAPL",
  "available_tickers": ["AAPL", "MSFT", "TSLA", "GOOGL"],
  "period": "1mo",
  "interval": "1d"
}
```

4️⃣ Run the web server:

```bash
python api_server.py
```

5️⃣ Open in your browser:

```
http://localhost:8000/
```

- Click **Run Analysis** button → this will:
  ✅ Fetch latest data
  ✅ Update report and plot
  ✅ Run ML prediction
  ✅ Show results + chart directly in the browser

---

## 🌐 API Endpoints

- **GET /** → main page with Run button
- **POST /run-scheduler** → manually trigger data update
- **GET /report/{ticker}** → get latest HTML report
- **GET /predict/{ticker}** → get ML prediction as JSON

Example:

```bash
curl -X POST http://localhost:8000/run-scheduler
```

---

## 📁 Output Files

- CSV files → stored in `/data`
- Plots and HTML reports → stored in `/reports`

Example:

- `reports/AAPL_report.html`
- `reports/AAPL_chart.png`

---

## 🏆 Author

Made by MDautev
🔗 GitHub: [github.com/MDautev](https://github.com/MDautev)

---

```

```
