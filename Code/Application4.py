from sklearn.linear_model import LinearRegression

X = [
    [2, 25000, 1200],
    [5, 60000, 1500],
    [3, 40000, 1300],
    [7, 90000, 1800],
    [1, 15000, 1000]
]

y = [650000, 420000, 520000, 300000, 720000]

model = LinearRegression()
model.fit(X, y)

age = int(input("Enter Car Age: "))
kms = int(input("Enter Kilometers Driven: "))
engine = int(input("Enter Engine CC: "))

price = model.predict([[age, kms, engine]])

print("Estimated Resale Price = ₹", price[0])
