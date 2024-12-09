import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
file_path = r'E:\ai lab task 9\Marvel_Movies_Dataset.csv'
df = pd.read_csv(file_path)
print("Initial Dataset Shape:", df.shape)
df.fillna(method='ffill', inplace=True) 
categorical_cols = df.select_dtypes(include=['object']).columns
label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le
scaler = StandardScaler()
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
X = df.drop(columns=['your_target_column']) 
y = df['your_target_column']  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
svm = SVC(kernel='linear') 
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))
processed_file_path = r'E:\ai lab task 9\Processed_Marvel_Movies_Dataset.csv'
df.to_csv(processed_file_path, index=False)
print("Processed data saved to:", processed_file_path)
