# Purpose - Create Data Model for Machine Learning
from sklearn.linear_model import LinearRegression
import pickle

#Example dataset
houseDataSet = [[1000, 2],[2200, 3], [4000, 4], [6000, 5]] #Features: [Area, Rooms]
price = [200000, 370000, 600000, 850000] #Target: Price


#Submit this data to machine learnong Linear Regression model
model = LinearRegression()
model.fit(houseDataSet, price)

#open the dataset in binary format and dump i.e save model in .pkl file
with open("house_price_model.pkl", "wb") as file:
    pickle.dump(model, file)