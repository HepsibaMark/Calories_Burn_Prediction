# 🔥 Calories Burn Prediction System Using Machine Learning

A machine learning-based web application that predicts the estimated number of calories burned during exercise.

## 🚀 Live Demo

👉 [Click here to use the Calories Burn Prediction App](PASTE_APP_LINK_HERE)

## 📌 Project Overview

The system predicts calories burned based on:

- Gender
- Age
- Height
- Weight
- Exercise Duration
- Heart Rate
- Body Temperature

The project uses an **XGBoost Regression** model and a **Gradio** web interface.

## 🧠 Machine Learning Model

**Model:** XGBoost Regressor

**Features:**

- Gender
- Age
- Height
- Weight
- Duration
- Heart Rate
- Body Temperature

**Target:** Calories

## 📊 Model Performance

- **MAE:** 1.51 kcal
- **R² Score:** 0.9988

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Gradio
- Matplotlib
- Seaborn
- Git
- GitHub

## 📂 Project Structure

```text
Calories_Burn_Prediction/
│
├── app.py
├── calories.csv
├── exercise.csv
├── calories_xgboost_model.json
├── requirements.txt
├── Calories_Burn_Prediction_Project_Report.docx
├── README.md
└── .gitignore
```

Then add the remaining sections:

````markdown
## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/HepsibaMark/Calories_Burn_Prediction.git
```

### 2. Open the project folder

```bash
cd Calories_Burn_Prediction
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

## 🔮 Workflow

```text
User Input
    ↓
Data Preprocessing
    ↓
XGBoost Regression Model
    ↓
Calories Prediction
    ↓
Gradio Web Interface
```

## 👩‍💻 Author

**Hepsiba Selvi M**

B.Tech Artificial Intelligence and Data Science

GitHub: https://github.com/HepsibaMark

## 📜 License

This project is created for academic and educational purposes.