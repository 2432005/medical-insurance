import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Set page config
st.set_page_config(
    page_title="Medical Cost Prediction",
    page_icon="🏥",
    layout="wide"
)

# Title and description
st.title("🏥 Medical Insurance Cost Prediction")
st.markdown("Predict your medical insurance cost using Machine Learning (Random Forest Regressor)")
st.markdown("---")

# Load the model
@st.cache_resource
def load_model():
    model = joblib.load('rf_tuned.pkl')
    return model

try:
    model = load_model()
except FileNotFoundError:
    st.error("❌ Model file 'rf_tuned.pkl' not found. Please ensure it's in the same directory.")
    st.stop()

# Create two columns for layout
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📋 Enter Your Information")
    
    # Input fields
    age = st.number_input(
        "Age (years)",
        min_value=18,
        max_value=100,
        value=30,
        help="Your age in years"
    )
    
    sex = st.selectbox(
        "Sex",
        options=["Male", "Female"],
        help="Select your gender"
    )
    sex_value = 1 if sex == "Male" else 0
    
    bmi = st.number_input(
        "BMI (Body Mass Index)",
        min_value=10.0,
        max_value=60.0,
        value=25.0,
        step=0.1,
        help="Your Body Mass Index"
    )
    
    children = st.number_input(
        "Number of Children",
        min_value=0,
        max_value=10,
        value=0,
        help="Number of dependent children"
    )
    
    smoker = st.selectbox(
        "Smoker",
        options=["No", "Yes"],
        help="Do you smoke?"
    )
    smoker_value = 1 if smoker == "Yes" else 0
    
    region = st.selectbox(
        "Region",
        options=["Southwest", "Southeast", "Northwest", "Northeast"],
        help="Your region of residence"
    )
    region_mapping = {
        "Southwest": 0,
        "Southeast": 1,
        "Northwest": 2,
        "Northeast": 3
    }
    region_value = region_mapping[region]

with col2:
    st.subheader("📊 Information Summary")
    
    # Display summary
    summary_data = {
        "Parameter": ["Age", "Sex", "BMI", "Children", "Smoker", "Region"],
        "Value": [f"{age} years", sex, f"{bmi:.1f}", f"{children}", smoker, region]
    }
    summary_df = pd.DataFrame(summary_data)
    st.table(summary_df)
    
    # Model info
    st.info("📌 **Model Information**\n\nModel: Random Forest Regressor\n\nAccuracy (R² Score): 94.25%\n\nThis model predicts annual medical insurance charges based on your profile.")

# Prediction section
st.markdown("---")

if st.button("🔮 Predict Insurance Cost", use_container_width=True, type="primary"):
    # Prepare features: [age, sex, bmi, children, smoker, region]
    features = [age, sex_value, bmi, children, smoker_value, region_value]
    final_features = np.array(features).reshape(1, -1)
    
    try:
        # Make prediction
        prediction = model.predict(final_features)[0]
        
        if prediction < 0:
            st.error("❌ Error calculating the amount!")
        else:
            # Display result
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.success("✅ Prediction Successful!")
                st.markdown(f"""
                ### Expected Annual Insurance Cost:
                # ${prediction:,.2f}
                """)
            
            with col2:
                st.metric(
                    label="Annual Cost",
                    value=f"${prediction:,.2f}",
                    delta=None
                )
            
            # Additional insights
            st.markdown("---")
            st.subheader("💡 Prediction Insights")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Monthly Cost (Approx.)", f"${prediction/12:,.2f}")
            with col2:
                st.metric("Weekly Cost (Approx.)", f"${prediction/52:,.2f}")
            with col3:
                st.metric("Daily Cost (Approx.)", f"${prediction/365:,.2f}")
                
    except Exception as e:
        st.error(f"❌ Error during prediction: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center">
    <p>Made with ❤️ | Medical Insurance Cost Prediction | Random Forest Model</p>
    <p style="font-size: 12px; color: gray;">Disclaimer: This prediction is for informational purposes only and should not be considered as actual insurance quotation.</p>
</div>
""", unsafe_allow_html=True)