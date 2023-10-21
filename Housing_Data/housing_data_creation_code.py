import pandas as pd
import numpy as np
# Define the number of data points
num_samples = 25
# Create random data for 'Area', 'Bedrooms', 'Bathrooms', and 'Garage'
np.random.seed(0)  # Set a seed for reproducibility
area = np.random.randint(1000, 4000, num_samples)
bedrooms = np.random.randint(2, 6, num_samples)
bathrooms = np.random.randint(1, 4, num_samples)
garage = np.random.randint(0, 3, num_samples)
# Create a linear relationship with some noise for 'Price'
price = 10000 + 300 * area + 2000 * bedrooms + 3000 * bathrooms + 1500 * garage + np.random.normal(0, 5000, num_samples)
# Create a DataFrame
data = pd.DataFrame({'Area': area, 'Bedrooms': bedrooms, 'Bathrooms': bathrooms, 'Garage': garage, 'Price': price})
# Save the DataFrame to a CSV file
data.to_csv('housing_data.csv', index=False)