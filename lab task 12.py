import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
train_df = pd.read_csv('train.csv') 
test_df = pd.read_csv('test.csv') 
print("Training Data Shape:", train_df.shape)
print("Testing Data Shape:", test_df.shape)
print("Training Data Info:\n", train_df.info())
train_df['Age'].fillna(train_df['Age'].median(), inplace=True)
test_df['Age'].fillna(test_df['Age'].median(), inplace=True)
train_df['Embarked'].fillna(train_df['Embarked'].mode()[0], inplace=True)
test_df['Fare'].fillna(test_df['Fare'].median(), inplace=True)
train_df.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'], inplace=True)
test_df.drop(columns=['Name', 'Ticket', 'Cabin'], inplace=True)
categorical_cols = ['Sex', 'Embarked']
for col in categorical_cols:
    le = LabelEncoder()
    train_df[col] = le.fit_transform(train_df[col])
    test_df[col] = le.transform(test_df[col])
X = train_df.drop(columns=['Survived'])
y = train_df['Survived']
scaler = StandardScaler()
X = scaler.fit_transform(X)
X_test = scaler.transform(test_df.drop(columns=['PassengerId']))
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_val_pred = model.predict(X_val)
print("\nValidation Accuracy:", accuracy_score(y_val, y_val_pred))
print("\nClassification Report:\n", classification_report(y_val, y_val_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_val, y_val_pred))
test_predictions = model.predict(X_test)
submission = pd.DataFrame({'PassengerId': test_df['PassengerId'], 'Survived': test_predictions})
submission_file = 'submission.csv'
submission.to_csv(submission_file, index=False)
print(f"Submission file saved as {submission_file}.")
