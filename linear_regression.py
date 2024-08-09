import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from numpy.polynomial.polynomial import Polynomial

file_path = 'daily_sales.csv'
df = pd.read_csv(file_path)

# Extract the year and month for simplicity
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['YearMonth'] = df['date'].dt.to_period('M')

# Aggregate sales by YearMonth
df_agg = df.groupby('YearMonth')['sales'].sum().reset_index()

# Convert 'YearMonth' back to datetime for plotting
df_agg['YearMonth'] = df_agg['YearMonth'].dt.to_timestamp()

# Prepare the data for regression
X = np.array((df_agg['YearMonth'] - df_agg['YearMonth'].min()).dt.days).reshape(-1, 1)
y = df_agg['sales'].values

# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Create linear regression plot
plt.figure(figsize=(12, 6))
plt.plot(df_agg['YearMonth'], df_agg['sales'], color='blue', marker='o', linestyle='None', label='Sales')
plt.plot(df_agg['YearMonth'], y_pred, color='red', linewidth=2, linestyle='-', label='Regression Line')
plt.xlabel('Time')
plt.ylabel('Sales (sales)')
plt.title('Sales over Time')
plt.legend()
plt.grid(False)
plt.xticks(rotation=45)
plt.tight_layout()

# Calculate residuals
residuals = y - y_pred

# Fit a polynomial to the residuals
p = Polynomial.fit(X.flatten(), residuals, deg=7)

# Generate values for the trend line
trend_line = p(X.flatten())

# Create residual plot
plt.figure(figsize=(12, 6))
plt.scatter(df_agg['YearMonth'], residuals, color='grey', marker='o')
plt.plot(df_agg['YearMonth'], trend_line, color='blue', linewidth=2, linestyle='-', label='Trend Line')
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Residuals')
plt.title('Residuals Plot')
plt.legend()
plt.grid(False)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()