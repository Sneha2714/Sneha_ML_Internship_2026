
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error

# Load dataset
df = pd.read_csv("Dataset 2.csv")

# Q1
print("\nFirst 5 Records:")
print(df.head())

# Q2
print("\nRows and Columns:")
print(df.shape)

# Q3
print("\nColumn Names:")
print(df.columns.tolist())

# Q4
print("\nNumerical Columns:")
print(df.select_dtypes(include=['int64', 'float64']).columns.tolist())

print("\nCategorical Columns:")
print(df.select_dtypes(include=['object']).columns.tolist())

# Q5
print("\nMissing Values:")
print(df.isnull().sum())
# Q6
print("\nAverage Age of Users:")
print(df["Age"].mean())

# Q7
print("\nAverage Watch Hours Per Week:")
print(df["WatchHoursPerWeek"].mean())

# Q8
print("\nAverage Monthly Spending:")
print(df["MonthlySpend"].mean())

# Q9
print("\nUsers in Each Subscription Category:")
print(df["SubscriptionType"].value_counts())

# Q10
print("\nPercentage of Users Who Renewed Subscription:")
renewed_percentage = (df["SubscriptionRenewed"] == "Yes").mean() * 100
print(f"{renewed_percentage:.2f}%")
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
# Q11 - Encode categorical columns

le = LabelEncoder()

df["Gender"] = le.fit_transform(df["Gender"])
df["SubscriptionType"] = le.fit_transform(df["SubscriptionType"])
df["FavoriteGenre"] = le.fit_transform(df["FavoriteGenre"])
df["SubscriptionRenewed"] = le.fit_transform(df["SubscriptionRenewed"])

print("\nEncoded Dataset:")
print(df.head())
# Q12

X = df.drop("SubscriptionRenewed", axis=1)
y = df["SubscriptionRenewed"]

print("\nFeatures Shape:", X.shape)
print("Target Shape:", y.shape)
# Q13

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Q14 - Train Decision Tree Model

dt_model = DecisionTreeClassifier(random_state=42)

dt_model.fit(X_train, y_train)

y_pred_dt = dt_model.predict(X_test)

print("\nDecision Tree Model Trained Successfully")

# Q15 - Accuracy

dt_accuracy = accuracy_score(y_test, y_pred_dt)

print("\nDecision Tree Accuracy:")
print(dt_accuracy)

# Q16 - Confusion Matrix

cm = confusion_matrix(y_test, y_pred_dt)

print("\nConfusion Matrix:")
print(cm)
from sklearn.neighbors import KNeighborsClassifier

# Q17 - Train KNN Model

knn_model = KNeighborsClassifier(n_neighbors=5)

knn_model.fit(X_train, y_train)

y_pred_knn = knn_model.predict(X_test)

print("\nKNN Model Trained Successfully")
# Q18 - KNN Accuracy

knn_accuracy = accuracy_score(y_test, y_pred_knn)

print("\nKNN Accuracy:")
print(knn_accuracy)

print("\nModel Comparison:")
print("Decision Tree Accuracy =", dt_accuracy)
print("KNN Accuracy =", knn_accuracy)

if dt_accuracy > knn_accuracy:
    print("Decision Tree performs better.")
elif knn_accuracy > dt_accuracy:
    print("KNN performs better.")
else:
    print("Both models perform equally.")
    from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Q19 - Linear Regression

X_reg = df.drop("MonthlySpend", axis=1)
y_reg = df["MonthlySpend"]

X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg, y_reg,
    test_size=0.2,
    random_state=42
)

lr_model = LinearRegression()

lr_model.fit(X_train_reg, y_train_reg)

y_pred_reg = lr_model.predict(X_test_reg)

print("\nLinear Regression Model Trained Successfully")

mse = mean_squared_error(y_test_reg, y_pred_reg)

print("Mean Squared Error:")
print(mse)
# Q20 - Predict Monthly Spend for a New User

new_user = [[751, 25, 1, 1, 20, 2, 1, 15, 1]]

predicted_spend = lr_model.predict(new_user)

print("\nPredicted Monthly Spend for New User:")
print(predicted_spend[0])
