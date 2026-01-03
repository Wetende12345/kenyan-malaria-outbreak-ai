import psycopg2
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

try:
    conn = psycopg2.connect(
    dbname="ridehailing_ai_db",
    user="postgres",
    password="Mamapipi1234#",
    host="localhost",
    port="5432"
)
    cur = conn.cursor()
    
    # Check if tables have data
    cur.execute("SELECT COUNT(*) FROM malaria_cases")
    count = cur.fetchone()[0]
    if count == 0:
        print("No data in malaria_cases — run ingest_data.py first!")
        conn.close()
        exit()
    
    df = pd.read_sql("""
        SELECT 
            m.county, 
            m.year, 
            m.month, 
            m.cases,
            w.rainfall_mm, 
            w.temperature
        FROM malaria_cases m
        JOIN weather w ON m.county = w.county AND m.year = w.year AND m.month = w.month
        LIMIT 1000  -- Sample for speed
    """, conn)
    
    conn.close()
    
    print(f"Loaded {len(df)} records for training")
    print(df.head())
    
    X = df[['rainfall_mm', 'temperature', 'month']]
    y = df['cases']
    
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X, y)
    
    # Predict high-risk: heavy rain, warm, rainy month
    pred = model.predict([[200, 26, 4]])[0]
    
    risk = "HIGH" if pred > 800 else "MEDIUM" if pred > 400 else "LOW"
    
    print("\n=== Malaria Outbreak AI Prediction ===")
    print(f"Scenario: Heavy rainfall (200mm) + 26°C in April")
    print(f"Predicted cases: {pred:.0f}")
    print(f"Risk Level: {risk}")
    if risk == "HIGH":
        print("URGENT ALERT: Deploy mosquito nets, spraying, and community education!")
    elif risk == "MEDIUM":
        print("Monitor: Prepare health facilities")
    else:
        print("Low risk: Continue surveillance")
        
except Exception as e:
    print(f"Error: {e}")
    print("Make sure schema and data are loaded!")
