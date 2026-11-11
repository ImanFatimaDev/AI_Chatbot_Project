# ============================================
# DecodeLabs - Artificial Intelligence
# Project 2: Data Classification Using AI
# ============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import plot_tree



# 1. Load Dataset

iris = load_iris()

X = iris.data
y = iris.target

print("Dataset loaded successfully!")
print("Dataset shape:", X.shape)
print("Target classes:", iris.target_names)


# 2. Understand the Dataset

df = pd.DataFrame(X, columns=iris.feature_names)
df["target"] = y

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nClass names:")
print(iris.target_names)


# 3. Split Data into Training and Testing

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))



# 4. Create Classification Model

model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)



# 5. Train the Model

model.fit(X_train, y_train)

print("\nModel trained successfully!")


# 6. Make Predictions

y_pred = model.predict(X_test)


# 7. Check Accuracy

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)
print("Accuracy Percentage:", accuracy * 100, "%")



# 8. Classification Report


print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=iris.target_names
    )
)


# 9. Confusion Matrix


cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)


# 10. Test Model with New Data

new_flower = [[5.1, 3.5, 1.4, 0.2]]

prediction = model.predict(new_flower)

print("\nNew Flower Prediction:")
print(iris.target_names[prediction[0]])



# 11. Visualize Decision Tree

plt.figure(figsize=(15, 8))

plot_tree(
    model,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True
)

plt.title("Decision Tree Classification Model")
plt.show()