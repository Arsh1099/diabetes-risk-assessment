from ai_engine.inference_engine import assess_diabetes_risk


def run_test(name, data):

    result = assess_diabetes_risk(**data)

    print("\n==============================")
    print(name)
    print("==============================")

    print(f"Risk Level : {result['risk_level']}")
    print(f"Risk Score : {result['score']}")

    print("\nReasons:")

    for reason in result["reasons"]:
        print(f"- {reason}")


# --------------------------------------------------
# LOW RISK TEST
# --------------------------------------------------

run_test(
    "LOW RISK TEST",
    {
        "age": 25,
        "glucose": 90,
        "bmi": 22,
        "blood_pressure": 115,
        "family_history": "No",
        "physical_activity": "High"
    }
)


# --------------------------------------------------
# MODERATE RISK TEST
# --------------------------------------------------

run_test(
    "MODERATE RISK TEST",
    {
        "age": 45,
        "glucose": 110,
        "bmi": 27,
        "blood_pressure": 135,
        "family_history": "Yes",
        "physical_activity": "Moderate"
    }
)


# --------------------------------------------------
# HIGH RISK TEST
# --------------------------------------------------

run_test(
    "HIGH RISK TEST",
    {
        "age": 55,
        "glucose": 180,
        "bmi": 35,
        "blood_pressure": 150,
        "family_history": "Yes",
        "physical_activity": "Low"
    }
)