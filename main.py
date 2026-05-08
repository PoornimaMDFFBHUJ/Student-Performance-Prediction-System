# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv('student_data.csv')

# Convert target column (Pass/Fail → 1/0)
le = LabelEncoder()
data['Final_Result'] = le.fit_transform(data['Final_Result'])

# Features and Target
X = data[['Study_Hours',
          'Attendance',
          'Assignments',
          'Internal_Marks',
          'Sports_Hours',
          'Projects_Score']]

y = data['Final_Result']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# ---------------- USER INPUT ----------------

print("\nEnter Student Details:")

study_hours = float(input("Study Hours: "))
attendance = float(input("Attendance (%): "))
assignments = float(input("Assignments Score: "))
internal_marks = float(input("Internal Marks: "))
sports_hours = float(input("Sports Hours: "))
projects_score = float(input("Projects Score: "))

# Convert input into DataFrame
new_student = pd.DataFrame([[
    study_hours,
    attendance,
    assignments,
    internal_marks,
    sports_hours,
    projects_score
]], columns=[
    'Study_Hours',
    'Attendance',
    'Assignments',
    'Internal_Marks',
    'Sports_Hours',
    'Projects_Score'
])

# Predict result
prediction = model.predict(new_student)

# Output
print("\nPrediction Result:",
      "Pass" if prediction[0] == 1 else "Fail")

# ---------------- GRAPH ----------------

plt.bar(data.index, data['Attendance'])

plt.title("Attendance of Students")
plt.xlabel("Student Index")
plt.ylabel("Attendance")

plt.show()

sports = data['Sports_Hours'].value_counts()

plt.pie(sports, labels=sports.index, autopct='%1.1f%%')

plt.title("Sports Hours Distribution")

plt.show()

sns.scatterplot(x=data['Assignments'],
                y=data['Internal_Marks'],
                hue=data['Final_Result'])

plt.title("Assignments vs Internal Marks")
plt.xlabel("Assignments")
plt.ylabel("Internal Marks")

plt.show()

results = data['Final_Result'].value_counts()

plt.pie(results,
        labels=['Pass', 'Fail'],
        autopct='%1.1f%%')

plt.title("Pass vs Fail Percentage")

plt.show()


