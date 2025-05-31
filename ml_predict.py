import pandas as pd
import logging
from sklearn.ensemble import RandomForestClassifier

def predict_price_movement(df):
    """
    Simple ML model to predict if tomorrow's price will go up (1) or down (0).
    """
    try:
        df = df.dropna()
        df['Return'] = df['Close'].pct_change()
        df['Target'] = (df['Return'].shift(-1) > 0).astype(int)

        features = ['Close', 'MA20', 'Volatility']
        df = df.dropna()

        X = df[features]
        y = df['Target']

        model = RandomForestClassifier()
        model.fit(X, y)

        latest = df[features].iloc[-1].values.reshape(1, -1)
        prediction = model.predict(latest)[0]

        if prediction == 1:
            logging.info("📈 Prediction: Price will go UP tomorrow.")
        else:
            logging.info("📉 Prediction: Price will go DOWN tomorrow.")

        return prediction

    except Exception as e:
        logging.error(f"❌ Error in ML prediction: {e}")
        return None
