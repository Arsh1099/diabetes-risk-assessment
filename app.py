import streamlit as st

from ai_engine.inference_engine import assess_diabetes_risk


# ==================================================
# PAGE SETTINGS
# ==================================================

st.set_page_config(
    page_title="Diabetes Risk Assessment",
    page_icon="🩺",
    layout="centered"
)


# ==================================================
# TITLE
# ==================================================

st.title("🩺 Diabetes Risk Assessment")

st.subheader(
    "AI-Based Expert System"
)

st.write(
    "This system uses a knowledge base and rule-based "
    "inference engine to assess diabetes risk."
)

st.info(
    "Educational project only. This system is not a "
    "medical diagnostic tool."
)


# ==================================================
# INPUTS
# ==================================================

st.header("Enter Your Information")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=25
    )

    glucose = st.number_input(
        "Fasting Glucose (mg/dL)",
        min_value=1,
        max_value=300,
        value=90
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=70.0,
        value=22.0,
        step=0.1
    )


with col2:

    blood_pressure = st.number_input(
        "Blood Pressure",
        min_value=50,
        max_value=200,
        value=115
    )

    family_history = st.selectbox(
        "Family History of Diabetes",
        ["No", "Yes"]
    )

    physical_activity = st.selectbox(
        "Physical Activity",
        ["High", "Moderate", "Low"]
    )


# ==================================================
# BUTTON
# ==================================================

st.write("")

if st.button(
    "🔍 Assess Diabetes Risk",
    use_container_width=True
):

    # ------------------------------------------------
    # RUN AI ENGINE
    # ------------------------------------------------

    result = assess_diabetes_risk(
        age=age,
        glucose=glucose,
        bmi=bmi,
        blood_pressure=blood_pressure,
        family_history=family_history,
        physical_activity=physical_activity
    )

    risk_level = result["risk_level"]
    score = result["score"]
    reasons = result["reasons"]
    triggered_rules = result["triggered_rules"]


    # ==================================================
    # RESULT
    # ==================================================

    st.header("Assessment Result")

    if risk_level == "HIGH RISK":

        st.error(
            f"🔴 HIGH RISK\n\n"
            f"Rule-Based Risk Score: {score}"
        )

    elif risk_level == "MODERATE RISK":

        st.warning(
            f"🟠 MODERATE RISK\n\n"
            f"Rule-Based Risk Score: {score}"
        )

    else:

        st.success(
            f"🟢 LOW RISK\n\n"
            f"Rule-Based Risk Score: {score}"
        )


    # ==================================================
    # AI REASONING SUMMARY
    # ==================================================

    st.header("🧠 AI Reasoning Summary")

    st.write(
        "The AI system examined the values entered by the user "
        "and compared them with the rules stored in its "
        "knowledge base."
    )

    st.write(
        "The inference engine evaluated the applicable rules "
        "and combined their results to generate the final "
        "risk assessment."
    )


    # ==================================================
    # REASONS
    # ==================================================

    st.header("⚠️ Why did the system reach this result?")


    if len(reasons) > 0:

        for reason in reasons:

            st.markdown(
                f"### • {reason}"
            )

    else:

        st.success(
            "No major higher-risk factors were identified "
            "by the current rule set."
        )


    # ==================================================
    # RULES
    # ==================================================

    st.header("📋 Rules Triggered")


    if len(triggered_rules) > 0:

        for rule in triggered_rules:

            st.write(
                f"**{rule['rule']}**"
            )

            st.write(
                f"Level: {rule['level'].capitalize()}"
            )

            st.write(
                f"Rule contribution: {rule['points']} point(s)"
            )

            st.write(
                f"Reason: {rule['reason']}"
            )

            st.divider()

    else:

        st.write(
            "No rules were triggered."
        )


    # ==================================================
    # HOW AI REASONED
    # ==================================================

    st.header("💡 How the AI Reached the Result")


    if risk_level == "HIGH RISK":

        st.write(
            "The inference engine identified an important "
            "risk factor or several risk factors occurring "
            "together. Based on the current rule set, the "
            "system classified the assessment as HIGH RISK."
        )

    elif risk_level == "MODERATE RISK":

        st.write(
            "The inference engine identified meaningful "
            "risk factors, but the combination did not meet "
            "the stronger conditions used for HIGH RISK. "
            "The system therefore classified the assessment "
            "as MODERATE RISK."
        )

    else:

        st.write(
            "The inference engine identified few or no "
            "important risk factors according to the current "
            "knowledge base. The system therefore classified "
            "the assessment as LOW RISK."
        )


    # ==================================================
    # GENERAL GUIDANCE
    # ==================================================

    st.header("🌿 General Health Guidance")

    st.write(
        "Regular physical activity, balanced eating habits, "
        "maintaining a healthy body weight and appropriate "
        "health check-ups support general health."
    )

    st.caption(
        "This is general educational information and not "
        "medical advice."
    )


# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "CODETECH Artificial Intelligence Internship"
)

st.caption(
    "Educational expert system — not a medical diagnostic system."
)