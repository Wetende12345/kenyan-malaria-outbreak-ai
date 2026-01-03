# 🏥 Kenyan Malaria Outbreak AI Predictor 🇰🇪

AI system to predict malaria outbreaks in Kenya using weather data (rainfall, temperature) and historical cases.

## 🎯 Impact
- Predicts high-risk periods for early intervention
- Helps health authorities deploy mosquito nets, spraying, education
- Can reduce cases and save lives in high-burden counties

## 🛠️ Tech Stack
- Python (pandas, scikit-learn)
- PostgreSQL warehouse
- Simulated data for 8 counties (2020-2025)

## 📊 Features
- Data ingestion (weather + cases)
- RandomForest model for case prediction
- Risk levels (LOW/MEDIUM/HIGH) with alerts

## 🚀 Run Locally
1. Clone repo
2. Create venv: `python3 -m venv venv && source venv/bin/activate`
3. Install: `pip install psycopg2-binary pandas scikit-learn`
4. Setup PostgreSQL DB `health_ai_db`
5. Run schema: `sudo -u postgres psql -d health_ai_db -f schema/create_tables.sql`
6. Load data: `python etl/ingest_data.py`
7. Run prediction: `python ai/outbreak_prediction.py`

## Sample Output
Predicted cases: 1245  
Risk Level: HIGH  
ALERT: Deploy mosquito nets and spraying!

Built by **Eden Wetende** — Data Engineer  
January 2026

Public health AI for Kenya — open for collaboration!

⭐ Star if you support health innovation!
