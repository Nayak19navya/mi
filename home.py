# home.py

import streamlit as st

def app():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")
    st.header("What is Cancer?")
    st.write("""
    Cancer is a group of diseases characterized by the uncontrolled growth and spread of abnormal cells.
    If not controlled, it can result in death. Cancer can start almost anywhere in the human body, which
    is made up of trillions of cells. Normally, human cells grow and multiply to form new cells as the
    body needs them. When cells grow old or become damaged, they die, and new cells take their place.
    However, sometimes this orderly process breaks down, and abnormal or damaged cells grow and multiply
    when they shouldn't.
    """)

    st.header("Key Facts about Cancer")
    st.write("""
    - **Leading Cause of Death**: Cancer is a leading cause of death worldwide, accounting for nearly 10 million deaths in 2020.
    - **Common Types**: The most common cancers are breast, lung, colon and rectum, and prostate cancers.
    - **Risk Factors**: Tobacco use, high body mass index, alcohol consumption, low fruit and vegetable intake, and lack of physical activity are significant risk factors.
    - **Early Detection**: Many cancers can be cured if detected early and treated effectively.
    """)

    st.header("Importance of Awareness")
    st.write("""
    Raising awareness about cancer is crucial for early detection and prevention. Public health campaigns,
    education, and regular screenings can help identify cancer at an early stage when treatment is more likely to be successful.
    Supporting cancer research and funding can also lead to better treatment options and potentially a cure.
    """)

    st.header("Support and Resources")
    st.write("""
    If you or someone you know is affected by cancer, there are many resources available for support.
    Organizations such as the American Cancer Society, Cancer Research UK, and others provide valuable information,
    resources, and support for patients and their families.
    """)

# To run the app function
if __name__ == "__main__":
    app()

