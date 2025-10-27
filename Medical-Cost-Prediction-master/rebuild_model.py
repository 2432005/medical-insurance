"""
Script to rebuild the Random Forest model with modern scikit-learn version
This recreates the model from the insurance.csv dataset
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

print("Loading dataset...")
df = pd.read_csv('insurance.csv')

print("Dataset shape:", df.shape)
print("Columns:", df.columns.tolist())

# Prepare data
X = df.drop('charges', axis=1)
y = df['charges']

# Encode categorical variables
le_sex = LabelEncoder()
le_smoker = LabelEncoder()
le_region = LabelEncoder()

X['sex'] = le_sex.fit_transform(X['sex'])
X['smoker'] = le_smoker.fit_transform(X['smoker'])
X['region'] = le_region.fit_transform(X['region'])

print("\nFeatures:", X.columns.tolist())
print("Feature shape:", X.shape)
print("Target shape:", y.shape)

# Train model
print("\nTraining Random Forest Regressor...")
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1,
    max_depth=20,
    min_samples_split=5,
    min_samples_leaf=2
)

model.fit(X, y)

# Evaluate
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

y_pred = model.predict(X)
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))
mae = mean_absolute_error(y, y_pred)

print(f"\nModel Performance:")
print(f"R² Score: {r2:.4f}")
print(f"RMSE: ${rmse:.2f}")
print(f"MAE: ${mae:.2f}")

# Save model
print("\nSaving model as rf_tuned.pkl...")
joblib.dump(model, 'rf_tuned.pkl')
print("✅ Model saved successfully!")

# Test prediction
print("\nTest prediction:")
test_features = np.array([30, 1, 25.0, 0, 0, 1]).reshape(1, -1)  # age, sex, bmi, children, smoker, region
test_pred = model.predict(test_features)[0]
print(f"Sample input: [Age=30, Sex=Male, BMI=25.0, Children=0, Smoker=No, Region=Southeast]")
print(f"Predicted cost: ${test_pred:.2f}")