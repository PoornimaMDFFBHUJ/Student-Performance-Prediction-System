# 🎓 Student Performance Prediction System

## Project Overview

The **Student Performance Prediction System** is a Machine Learning-based project that predicts whether a student will **Pass or Fail** based on academic and behavioral factors such as study hours, attendance, and previous marks.

This project helps educational institutions identify **at-risk students early** and take corrective actions to improve their performance.

---

##  Objectives

* Predict student academic performance (Pass/Fail)
* Identify weak students at an early stage
* Support teachers with data-driven insights
* Improve overall academic outcomes

---

## Technologies Used

* **Programming Language:** Python
* **Libraries:**

  * Pandas (Data Handling)
  * NumPy (Numerical Computation)
  * Scikit-learn (Machine Learning)
  * Matplotlib / Seaborn (Visualization)
* **Tools:**

  * VS Code
  * Jupyter Notebook / Google Colab
  * Excel (Dataset)

---

## 📂 Project Structure

```
Student_Performance_Prediction/
│
├── main.py                # Main Python file
├── student_data.csv       # Dataset
├── venv/                  # Virtual environment
└── README.md              # Project documentation
```

---

##  Dataset Description

The dataset contains the following features:

| Feature Name   | Description                 |
| -------------- | --------------------------- |
| Student_ID     | Unique student identifier   |
| Study_Hours    | Daily study time            |
| Attendance     | Attendance percentage       |
| Previous_Marks | Previous exam scores        |
| Assignments    | Assignment scores           |
| Internal_Marks | Internal assessment marks   |
| Final_Result   | Target variable (Pass/Fail) |

---

##  How to Run the Project

### Step 1: Clone or Download Project

Download and extract the project folder.

### Step 2: Open in VS Code

```
File → Open Folder → Student_Performance_Prediction
```

### Step 3: Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

### Step 5: Run the Project

```bash
python main.py
```

---

##  Sample Output

###  Accuracy

```
Accuracy: 0.85
```

### 🔹 Prediction

```
Enter Student Details:
Study Hours: 6
Attendance (%): 90
Previous Marks: 85
Assignments Score: 88
Internal Marks: 87

Prediction Result: Pass
```

---

## Visualization

The system generates a scatter plot showing:

* Relationship between **Study Hours and Marks**
* Classification of students as **Pass/Fail**

---

## 🚀 Features

* Machine Learning-based prediction
* Interactive user input via terminal
* Data visualization using graphs
* Simple and easy-to-understand implementation

---

##  Advantages

* Early detection of weak students
* Improves teaching strategies
* Saves time for educators
* Data-driven decision making

---

##  Limitations

* Requires quality dataset
* Accuracy depends on data size
* Does not consider psychological factors

---

##  Future Enhancements

* GUI-based application (Tkinter/Web App)
* Real-time student monitoring
* Integration with Learning Management Systems (LMS)
* Advanced ML models (Random Forest, SVM)

---

## Conclusion

This project demonstrates how Machine Learning can be used to predict student performance and assist educational institutions in making smarter, data-driven decisions.

---

## 👩‍💻 Author

* Your Name

---
