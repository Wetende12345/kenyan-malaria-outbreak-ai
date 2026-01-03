import psycopg2
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

conn = psycopg2.connect(
    dbname="ridehailing_ai_db",
    user="denwetende",
    password="Mamapipi1234#",  # The one you just set
    host="localhost",
    port="5432"
)
df = pd.read_sql("""
    SELECT m.county, m.year, m.month, m.cases, w.rainfall_mm, w.temperature
    FROM malaria_cases m
    JOIN weather w ON m.county = w.county AND m.year = w.year AND m.month = w.month
""", conn)

conn.close()

X = df[['rainfall_mm', 'temperature', 'month']]
y = df['cases']

model = RandomForestRegressor()
model.fit(X, y)

# Predict for March 2026 (rainy season) in Kisumu
pred = model.predict([[200, 26, 3]])[0]  # High rain, warm, March
risk = "HIGH" if pred > 800 else "MEDIUM" if pred > 400 else "LOW"

print(f"Predicted malaria cases in Kisumu (March 2026): {pred:.0f}")
print(f"Risk Level: {risk} — Alert health authorities!")
