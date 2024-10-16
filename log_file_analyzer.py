
import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LogFileAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.model = IsolationForest(contamination=0.1)

    def load_data(self):
        logging.info("Loading log data...")
        self.data = pd.read_csv(self.log_file)
        logging.info("Data loaded successfully.")

    def preprocess_data(self):
        logging.info("Preprocessing data...")
        # Assuming the log file has columns 'timestamp', 'ip_address', 'event_type'
        self.data['timestamp'] = pd.to_datetime(self.data['timestamp'])
        self.data['ip_address'] = self.data['ip_address'].astype('category')
        self.data['event_type'] = self.data['event_type'].astype('category')

        # For this example, we convert categorical features to numeric using one-hot encoding
        self.data = pd.get_dummies(self.data, columns=['ip_address', 'event_type'])
        self.features = self.data.drop(['timestamp'], axis=1)  # Use all except timestamp as features
        logging.info("Data preprocessed successfully.")

    def train_model(self):
        logging.info("Training the model...")
        self.model.fit(self.features)
        logging.info("Model trained successfully.")

    def detect_intrusions(self):
        logging.info("Detecting intrusions...")
        predictions = self.model.predict(self.features)
        # In Isolation Forest, -1 indicates anomalies
        self.data['anomaly'] = np.where(predictions == -1, 1, 0)
        return self.data[self.data['anomaly'] == 1]  # Return only anomalies

if __name__ == "__main__":
    log_file_path = "path/to/your/log_file.csv"  # Update with your log file path
    analyzer = LogFileAnalyzer(log_file_path)
    
    analyzer.load_data()
    analyzer.preprocess_data()
    analyzer.train_model()
    anomalies = analyzer.detect_intrusions()
    
    if not anomalies.empty:
        print("Intrusions detected:")
        print(anomalies)
    else:
        print("No intrusions detected.")
