from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import joblib, numpy as np, pandas as pd, os

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

print("Loading model files...")
model         = joblib.load('churn_model_files/churn_model.pkl')
scaler        = joblib.load('churn_model_files/scaler.pkl')
feature_names = joblib.load('churn_model_files/feature_names.pkl')
print(f"✅ Model ready: {type(model).__name__}")
print(f"✅ Features: {feature_names}")

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        df   = pd.DataFrame([data])

        for feat in feature_names:
            if feat not in df.columns:
                df[feat] = 0

        df      = df[feature_names]
        scaled  = scaler.transform(df)
        pred    = int(model.predict(scaled)[0])
        proba   = model.predict_proba(scaled)[0].tolist()

        churn_prob = round(proba[1]*100, 1)
        stay_prob  = round(proba[0]*100, 1)

        if churn_prob < 30:   risk = 'low'
        elif churn_prob < 60: risk = 'medium'
        else:                 risk = 'high'

        print(f"✅ Predicted: {churn_prob}% churn — {risk} risk")

        return jsonify({
            'success'   : True,
            'churn_prob': churn_prob,
            'stay_prob' : stay_prob,
            'will_churn': pred == 1,
            'risk_level': risk,
            'model_name': type(model).__name__,
            'confidence': round(75 + abs(proba[1]-0.5)*40, 1)
        })

    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/health')
def health():
    return jsonify({'status':'ok','model':type(model).__name__})

if __name__ == '__main__':
    print("\n" + "="*45)
    print("🚀 ChurnIQ Server Running!")
    print("   Open: http://localhost:5000")
    print("="*45+"\n")
    app.run(debug=True, port=5000)