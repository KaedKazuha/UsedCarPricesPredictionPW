import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score  # Add r2_score here
import joblib


# Load the cleaned data
df = pd.read_csv('../JsonAndOtherData/better_cleaned_cars_data.csv')

# Encode categorical features
df = pd.get_dummies(df, columns=['fuel_type', 'transmission', 'location', 'make', 'model'])

# Split the data
X = df.drop(columns=['price'])
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)  # r2_score is now correctly imported

print('Mean Absolute Error:', mae)
print('R^2 Score:', r2)

model_filename = 'car_price_model.pkl'
joblib.dump(model, model_filename)