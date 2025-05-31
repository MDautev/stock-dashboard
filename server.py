from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
import uvicorn
import os
import logging
import json
from scheduler import job
from ml_predict import predict_price_movement
from process_data import process_data
from fastapi.staticfiles import StaticFiles



app = FastAPI()

app.mount("/static", StaticFiles(directory="reports"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Financial Dashboard</title>
        </head>
        <body>
            <h1>Financial Dashboard API</h1>
            <form action="/run-scheduler" method="post">
            <button type="submit">Run Analysis</button>
            </form>
        </body>
    </html>
    """

@app.post("/run-scheduler", response_class=HTMLResponse)
def run_scheduler(request: Request):
    try:
        logging.info("Manual trigger: running analysys job...")
        job()

        with open('config.json') as f:
            config = json.load(f)
        ticker = config.get('ticker', 'AAPL')
        chart_path = f"/static/{ticker}_chart.png"
        csv_path = f"data/{ticker}_data.csv"

        df = process_data(csv_path)
        last_change = ((df['Close'].iloc[-1] - df['Close'].iloc[0]) / df['Close'].iloc[0]) * 100
        avg_volatility = df['Volatility'].mean()
        prediction = predict_price_movement(df)

        prediction_text = "📈 UP tomorrow" if prediction == 1 else "📉 DOWN tomorrow"

        html_content = f"""
        <html>
            <head>
                <title>Scheduler Result</title>
            </head>
            <body>
                <h1>✅ Analysis completed successfully!!</h1>
                <h2>{ticker} Summary</h2>
                <p>Last 30 days change: {last_change:.2f}%</p>
                <p>Average volatility: {avg_volatility:.2f}</p>
                <p>ML Prediction: <strong>{prediction_text}</strong></p>
                <h3>Latest Chart</h3>
                <img src="{chart_path}" alt="Chart" width="600">
                <br><br>
                <a href="/">Back</a>
            </body>
        </html>
        """
        return HTMLResponse(content=html_content)
    except Exception as e:
        logging.error(f"❌ Error during Analysis run: {e}")
        return HTMLResponse(
            content=f"<h1>❌ Error: {e}</h1><a href='/'>Back</a>",
            status_code=500
        )




@app.get("/report/{ticker}")
def get_report(ticker: str):
    file_path = f"reports/{ticker}_report.html"
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type='text/html')
    return {"error": f"Report for {ticker} not found."}

@app.get("/predict/{ticker}")
def get_prediction(ticker: str):
    file_path = f"data/{ticker}_data.csv"
    if not os.path.exists(file_path):
        return {"error": f"No data file for {ticker}"}

    df = process_data(file_path)
    if df is None:
        return {"error": "Data processing failed"}

    prediction = predict_price_movement(df)
    if prediction == 1:
        result = "UP"
    elif prediction == 0:
        result = "DOWN"
    else:
        result = "UNKNOWN"

    return {"ticker": ticker, "prediction": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

