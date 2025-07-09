import sys
import joblib
import pandas as pd
from extract_features import extract_features

if len(sys.argv) != 2:
    print("Usage: python3 predict.py path_to_pcap")
    sys.exit(1)

pcap_file = sys.argv[1]
features = extract_features(pcap_file)
if features:
    X = pd.DataFrame([features])
    scaler = joblib.load("scaler.pkl")
    model = joblib.load("phishing_detector_model.pkl")

    X_scaled = scaler.transform(X)
    prediction = model.predict(X_scaled)
    print("Prediction:", "Phishing" if prediction[0] == 0 else "Legitimate")
else:
    print("Could not extract features from provided pcap file.")

