from sklearn.linear_model import LogisticRegression

X = [
    [1, 3, 120],
    [6, 15, 300],
    [0, 1, 80],
    [4, 10, 250],
    [2, 5, 160]
]

y = [0, 1, 0, 1, 0]

model = LogisticRegression()
model.fit(X, y)

links = int(input("Enter Number of Links: "))
caps = int(input("Enter Number of Capitalized Words: "))
length = int(input("Enter Email Length: "))

prediction = model.predict([[links, caps, length]])

if prediction[0] == 1:
    print("Spam Email")
else:
    print("Not Spam")