import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Generate sample data
np.random.seed(42)
num_samples = 1000

ages = np.random.randint(18, 65, num_samples)
genders = np.random.randint(0, 2, num_samples)
fever = np.random.randint(0, 2, num_samples)
fatigue = np.random.randint(0, 2, num_samples)
rash = np.random.randint(0, 2, num_samples)
risky_behavior = np.random.randint(0, 2, num_samples)
test_results = np.random.randint(0, 2, num_samples)

data = pd.DataFrame({
    'Age': ages,
    'Gender': genders,
    'Fever': fever,
    'Fatigue': fatigue,
    'Rash': rash,
    'RiskyBehavior': risky_behavior,
    'TestResult': test_results
})

# Split data into features (X) and the target variable (y)
X = data.drop('TestResult', axis=1)  # Features
y = data['TestResult']  # Target variable

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a decision tree classifier
clf = DecisionTreeClassifier()

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions on the test set
predictions = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
conf_matrix = confusion_matrix(y_test, predictions)
report = classification_report(y_test, predictions)

print("Accuracy:", accuracy)
print("\nConfusion Matrix:\n", conf_matrix)
print("\nClassification Report:\n", report)
