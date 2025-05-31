import pandas as pd
import os
import logging

def process_data(file_path='data/AAPL_data.csv'):
    """
    Process and clean the data, adding indicators.
    :param file_path: Path to the CSV file
    :return: Processed DataFrame or None if failed
    """
    try:
        if not os.path.exists(file_path):
            logging.warning(f" CSV file {file_path} does not exist.")
            return None

        logging.info(f"Loading data from {file_path}...")
        df = pd.read_csv(file_path, index_col=0, parse_dates=True)
        

        logging.info("Cleaning missing values...")
        df = df.dropna()

        df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
        df = df.dropna(subset=['Close'])

        logging.info(" Calculating indicators (MA20, Volatility)...")
        df['MA20'] = df['Close'].rolling(window=20).mean()
        df['Volatility'] = df['Close'].rolling(window=20).std()

        logging.info(" Data processing completed.")
        return df

    except Exception as e:
        logging.error(f" Error during data processing: {e}")
        return None

if __name__ == "__main__":
    import logging
    from logging_setup import setup_logging

    setup_logging()
    df = process_data()
    if df is not None:
        logging.info(df.tail())

