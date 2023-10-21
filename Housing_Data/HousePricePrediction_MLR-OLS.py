import pandas as pd
import statsmodels.api as sm

# Load Dataset
data = pd.read_csv('housing_data.csv')
X = data[['Area', 'Bedrooms', 'Bathrooms', 'Garage']]
y = data[['Price']]

# Add a constant term for intercept
X = sm.add_constant(X)

# Fit the multiple linear regression model
model = sm.OLS(y, X).fit()

# Get the model summary
model_summary = model.summary()
print(model_summary)

new_data = [[1, 2000, 3, 2, 2]]
new_data = sm.add_constant(new_data)

#Make predictions using the fitted medel
predictions = model.predict(new_data)
print("Predicted Value:", predictions[0])
