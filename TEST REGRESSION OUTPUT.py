import pandas as pd
import statsmodels.api as sm

# Create the dataframe
data = {
    'Company': ['A', 'B', 'C', 'D', 'E'],
    'Revenue': [1200, 1500, 1700, 1300, 1600],
    'Sales Volume': [1000, 1200, 1300, 1100, 1250],
    'Advertising Spend': [200, 250, 300, 220, 270],
    'Customer Count': [1500, 1800, 2000, 1600, 1900]
}

df = pd.DataFrame(data)

# Define the predictor variables and the target variable
X = df[['Customer Count']]
y = df['Revenue']

# Add a constant to the model (intercept)
X = sm.add_constant(X)

# Fit the multiple regression model
model = sm.OLS(y, X).fit()

# Print the summary of the regression analysis
print(model.summary())
