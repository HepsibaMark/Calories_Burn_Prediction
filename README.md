# 🔥 Calories Burn Prediction System Using Machine Learning

A machine learning-based web application that predicts the estimated number of calories burned during exercise.

## 🔗 Project Repository

👉 [View the project on GitHub](https://github.com/HepsibaMark/Calories_Burn_Prediction)

## 📌 Project Overview

The system predicts calories burned based on the following input features:

- Gender
- Age
- Height
- Weight
- Exercise Duration
- Heart Rate
- Body Temperature

The project uses an **XGBoost Regression** model for prediction and a **Gradio** web interface for user interaction.

## 🧠 Machine Learning Model

**Model:** XGBoost Regressor

### Features

- Gender
- Age
- Height
- Weight
- Duration
- Heart Rate
- Body Temperature

### Target

- Calories

## 📊 Model Performance

- **Mean Absolute Error (MAE):** 1.51 kcal
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

## ▶️ Run the Application Locally

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

The Gradio application will open locally in your browser.

## 🔮 Project Workflow

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

## 📈 Prediction Inputs

The user provides:

1. Gender
2. Age
3. Height
4. Weight
5. Exercise Duration
6. Heart Rate
7. Body Temperature

The trained XGBoost model processes these inputs and provides the estimated calories burned.

## 👩‍💻 Author

**Hepsiba Selvi M**

B.Tech Artificial Intelligence and Data Science

GitHub: [HepsibaMark](https://github.com/HepsibaMark)

## 📜 License

This project is created for academic and educational purposes.