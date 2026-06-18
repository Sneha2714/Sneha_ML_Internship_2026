import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import pandas as pd

# Load Dataset
df = pd.read_csv("week3ass.csv")

# Q1
print("\n===== Q1 Dataset Overview =====")

print("\nRows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 10 Records:")
print(df.head(10))
# Q2 - Data Types and Missing Values
print("\n===== Q2 Data Types and Missing Values =====")

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())


# Q3 - Descriptive Statistics
print("\n===== Q3 Descriptive Statistics =====")

stats = df.describe()

print(stats)

print("\nHighest Mean Value Feature:")
print(stats.loc['mean'].idxmax())

print("\nHighest Standard Deviation Feature:")
print(stats.loc['std'].idxmax())


# Q4 - Average Yield
print("\n===== Q4 Average Crop Yield =====")

print("Average Yield:")
print(df["yield_ton_per_hectare"].mean())


# Q5 - Crop Type Distribution
print("\n===== Q5 Crop Type Distribution =====")

print(df["crop_type"].value_counts())


# Q6 - Soil Type Distribution
print("\n===== Q6 Soil Type Distribution =====")

print(df["soil_type"].value_counts())


# Q7 - Correlation Analysis
print("\n===== Q7 Correlation Analysis =====")

numeric_df = df.select_dtypes(include=['float64', 'int64'])

print(numeric_df.corr())
# Q8 - Histogram

df.hist(figsize=(10, 8))
plt.suptitle("Histograms of Numerical Features")
plt.show()
# Q9 - Scatter Plot

plt.figure(figsize=(8,5))
plt.scatter(df["fertilizer_kg"], df["yield_ton_per_hectare"])
plt.xlabel("Fertilizer (kg)")
plt.ylabel("Yield (ton/hectare)")
plt.title("Fertilizer vs Yield")
plt.show()
# Q10 - Correlation Heatmap

plt.figure(figsize=(8,6))

sns.heatmap(
    numeric_df.corr(),
    annot=True
)

plt.title("Correlation Heatmap")
plt.show()
# Q11 - Label Encoding

le = LabelEncoder()

df["crop_type"] = le.fit_transform(df["crop_type"])
df["soil_type"] = le.fit_transform(df["soil_type"])

print("\nCategorical Columns Encoded Successfully")
# Q12

X = df.drop("yield_ton_per_hectare", axis=1)
y = df["yield_ton_per_hectare"]

print("\nFeatures Shape:", X.shape)
print("Target Shape:", y.shape)
# Q13

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)
# Q14

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(
    y_test,
    predictions
)

r2 = r2_score(
    y_test,
    predictions
)

print("\n===== MODEL RESULTS =====")

print("Mean Absolute Error:")
print(mae)

print("\nR2 Score:")
print(r2)
