import streamlit as st
import pandas as pd
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Data Explorer Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📌 Menu")
page = st.sidebar.radio(
    "Navigate",
    ["Home", "Dataset", "Visualizations", "User Form", "About App"]
)

# ---------------- HOME PAGE ----------------
if page == "Home":
    st.title("📊 Data Explorer Dashboard")
    st.write("An interactive web app to explore data and visualizations.")

    st.info("Use the sidebar to switch between sections.")

    name = st.text_input("Enter your name")
    if name:
        st.success(f"Welcome, {name}! 👋")

# ---------------- DATA PAGE ----------------
elif page == "Dataset":
    st.title("📂 Sample Dataset")

    data = pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie", "David"],
        "Age": [25, 30, 35, 40],
        "Score": [85, 90, 78, 92]
    })

    st.dataframe(data, use_container_width=True)

    st.download_button(
        label="⬇️ Download CSV",
        data=data.to_csv(index=False),
        file_name="sample_data.csv",
        mime="text/csv"
    )

# ---------------- CHARTS PAGE ----------------
elif page == "Visualizations":
    st.title("📈 Data Visualizations")

    chart_data = pd.DataFrame(
        np.random.randn(50, 3),
        columns=["Feature A", "Feature B", "Feature C"]
    )

    st.subheader("Line Chart")
    st.line_chart(chart_data)

    st.subheader("Bar Chart")
    st.bar_chart(chart_data)

# ---------------- FORM PAGE ----------------
elif page == "User Form":
    st.title("📝 User Information Form")

    with st.form("user_form"):
        username = st.text_input("Username")
        email = st.text_input("Email")
        age = st.number_input("Age", min_value=0, max_value=120)
        submitted = st.form_submit_button("Submit")

    if submitted:
        st.success("✅ Form submitted successfully!")
        st.write("### Submitted Details")
        st.write(f"**Username:** {username}")
        st.write(f"**Email:** {email}")
        st.write(f"**Age:** {age}")

# ---------------- ABOUT PAGE ----------------
elif page == "About App":
    st.title("ℹ️ About This Application")
    st.write("""
    **Data Explorer Dashboard** is use to see multiple data and dataframe from the user.

    ### Features:
    - Sidebar navigation
    - Data table display
    - Interactive charts
    - User input forms

   
    """)

    st.markdown("🚀 Future scope: ML models, predictions, database integration")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("© 2025 | Data Explorer Dashboard")
