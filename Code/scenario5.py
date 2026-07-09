from sklearn.tree import DecisionTreeClassifier, export_text

X = [
    [45000, 720, 0],
    [30000, 650, 1],
    [60000, 780, 0],
    [28000, 620, 2],
    [52000, 710, 1]
]

y = [1, 0, 1, 0, 1]

model = DecisionTreeClassifier(criterion="gini")
model.fit(X, y)

income = int(input("Enter Income: "))
credit = int(input("Enter Credit Score: "))
loans = int(input("Enter Existing Loans: "))

prediction = model.predict([[income, credit, loans]])

if prediction[0] == 1:
    print("Loan Approved")
else:
    print("Loan Rejected")

rules = export_text(
    model,
    feature_names=["Income", "Credit_Score", "Existing_Loans"]
)

print("\nDecision Rules:\n")
print(rules)