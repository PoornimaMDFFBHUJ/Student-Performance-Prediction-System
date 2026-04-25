# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv('student_data.csv')

# Convert target (Pass/Fail → 1/0)
le = LabelEncoder()
data['Final_Result'] = le.fit_transform(data['Final_Result'])

# Features and Target
X = data[['Study_Hours', 'Attendance', 'Previous_Marks', 'Assignments', 'Internal_Marks']]
y = data['Final_Result']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nReport:\n", classification_report(y_test, y_pred))

# Take input from user
print("\nEnter Student Details:")

study_hours = float(input("Study Hours: "))
attendance = float(input("Attendance (%): "))
previous_marks = float(input("Previous Marks: "))
assignments = float(input("Assignments Score: "))
internal_marks = float(input("Internal Marks: "))

# Convert to DataFrame
import pandas as pd
new_student = pd.DataFrame([[study_hours, attendance, previous_marks, assignments, internal_marks]],
columns=['Study_Hours', 'Attendance', 'Previous_Marks', 'Assignments', 'Internal_Marks'])

# Prediction
prediction = model.predict(new_student)

# Output
print("\nPrediction Result:", "Pass" if prediction[0] == 1 else "Fail")
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x=data['Study_Hours'], y=data['Previous_Marks'], hue=data['Final_Result'])

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Previous Marks")

plt.show()