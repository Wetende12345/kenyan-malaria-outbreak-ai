CREATE TABLE malaria_cases (
    id SERIAL PRIMARY KEY,
    county VARCHAR(100),
    year INT,
    month INT,
    cases INT,
    deaths INT
);

CREATE TABLE weather (
    id SERIAL PRIMARY KEY,
    county VARCHAR(100),
    year INT,
    month INT,
    rainfall_mm DECIMAL(6,2),
    temperature DECIMAL(4,2)
);

CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    county VARCHAR(100),
    crop_type VARCHAR(50),
    predicted_month DATE,
    risk_level VARCHAR(20),
    predicted_cases INT
);
