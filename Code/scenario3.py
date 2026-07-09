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

new_email = [[3, 8, 200]]

prediction = model.predict(new_email)

print("Prediction:", "Spam" if prediction[0] == 1 else "Not Spam")