import gradio as gr
import pandas as pd
from xgboost import XGBRegressor


# Load trained model
model = XGBRegressor()
model.load_model("calories_xgboost_model.json")


# Prediction function
def predict_calories(
    gender,
    age,
    height,
    weight,
    duration,
    heart_rate,
    body_temp
):

    # Check gender
    if gender is None:
        return "⚠️ Please select Gender."

    # Check empty values
    values = [
        age,
        height,
        weight,
        duration,
        heart_rate,
        body_temp
    ]

    if any(value is None for value in values):
        return "⚠️ Please fill in all the fields."

    # Basic validation
    if age <= 0:
        return "⚠️ Age must be greater than 0."

    if height <= 0:
        return "⚠️ Height must be greater than 0."

    if weight <= 0:
        return "⚠️ Weight must be greater than 0."

    if duration <= 0:
        return "⚠️ Exercise duration must be greater than 0."

    if heart_rate <= 0:
        return "⚠️ Heart rate must be greater than 0."

    if body_temp <= 0:
        return "⚠️ Body temperature must be greater than 0."

    # Gender encoding
    gender_value = 0 if gender == "Male" else 1

    # Create input data
    user_data = pd.DataFrame({
        "Gender": [gender_value],
        "Age": [age],
        "Height": [height],
        "Weight": [weight],
        "Duration": [duration],
        "Heart_Rate": [heart_rate],
        "Body_Temp": [body_temp]
    })

    # Prediction
    prediction = model.predict(user_data)[0]

    return f"🔥 Estimated Calories Burned: {prediction:.2f} kcal"


# Clear function
def clear_all():
    return None, None, None, None, None, None, None, ""


# Create application
with gr.Blocks(
    title="Calories Burn Prediction System"
) as demo:

    gr.Markdown(
        """
        # 🔥 Calories Burn Prediction System

        ### Machine Learning Based Calorie Estimation

        Enter your personal and exercise details to estimate
        the calories burned.
        """
    )

    gr.Markdown("### 👤 Personal & Exercise Details")

    with gr.Row():

        with gr.Column():

            gender = gr.Radio(
                ["Male", "Female"],
                label="Gender"
            )

            age = gr.Number(
                label="Age",
                minimum=1,
                placeholder="Enter your age"
            )

            height = gr.Number(
                label="Height (cm)",
                minimum=1,
                placeholder="Example: 159"
            )

            weight = gr.Number(
                label="Weight (kg)",
                minimum=1,
                placeholder="Example: 48"
            )

        with gr.Column():

            duration = gr.Number(
                label="Exercise Duration (minutes)",
                minimum=1,
                placeholder="Example: 60"
            )

            heart_rate = gr.Number(
                label="Heart Rate",
                minimum=1,
                placeholder="Example: 100"
            )

            body_temp = gr.Number(
                label="Body Temperature (°C)",
                minimum=1,
                placeholder="Example: 40"
            )

    gr.Markdown("### 📊 Prediction")

    output = gr.Textbox(
        label="Result",
        placeholder="Your predicted calories will appear here..."
    )

    with gr.Row():

        predict_button = gr.Button(
            "🔥 Predict Calories",
            variant="primary"
        )

        clear_button = gr.Button(
            "🧹 Clear"
        )

    predict_button.click(
        fn=predict_calories,
        inputs=[
            gender,
            age,
            height,
            weight,
            duration,
            heart_rate,
            body_temp
        ],
        outputs=output
    )

    clear_button.click(
        fn=clear_all,
        inputs=[],
        outputs=[
            gender,
            age,
            height,
            weight,
            duration,
            heart_rate,
            body_temp,
            output
        ]
    )

    gr.Markdown(
        """
        ---
        **Model:** XGBoost Regressor  
        **Features:** Gender, Age, Height, Weight, Duration, Heart Rate, Body Temperature  
        **Target:** Calories Burned
        """
    )


# Launch application
demo.launch(
    share=True,
    theme=gr.themes.Soft()
)