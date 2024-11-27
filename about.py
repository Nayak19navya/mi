import streamlit as st

def app():
    st.title("There is 'can' in cancer because we can beat it")

    st.header("Breast Cancer Detection Using Deep Learning")
    
    st.write("""
    **Innovative Detection Method:** Our website utilizes advanced deep learning models to analyze ultrasound images and detect breast cancer. This cutting-edge technology provides an accurate and efficient way to identify cancerous tissues, aiding in early diagnosis and treatment.
    """)

    st.header("How It Works:")
    
    st.write("""
    - **Ultrasound Imaging:** Ultrasound images are used for their ability to provide detailed visuals of breast tissues. These images help in distinguishing between benign and malignant growths.
    - **Deep Learning Model:** Our deep learning model is trained on vast datasets of labeled ultrasound images. By learning the patterns associated with cancerous and non-cancerous tissues, the model can make predictions with high accuracy.
    - **Detection Results:** Once an ultrasound image is uploaded, our model processes it to determine the likelihood of it being cancerous. The results are quick and reliable, enabling timely medical consultation and intervention.
    """)

    st.header("Benefits of Our Approach:")
    
    st.write("""
    - **Accuracy:** High accuracy in detecting cancerous tissues, reducing false positives and negatives.
    - **Speed:** Faster diagnosis compared to traditional methods, allowing for prompt treatment decisions.
    - **Non-Invasive:** Utilizes ultrasound imaging, which is a non-invasive and widely accessible diagnostic tool.
    """)

    st.header("Importance of Early Detection")
    
    st.write("""
    Early detection is crucial in the fight against breast cancer. By leveraging advanced deep learning technology, we aim to improve early diagnosis rates and provide critical support in the timely treatment of breast cancer.
    """)

# To run the app function
if __name__ == "__main__":
    app()
