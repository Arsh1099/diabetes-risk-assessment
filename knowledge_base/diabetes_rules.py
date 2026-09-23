"""
Knowledge Base for Diabetes Risk Assessment

This module contains the rules used by the
AI expert system to assess diabetes risk.
"""


def assess_glucose(glucose):
    """
    Assess risk based on glucose level.
    """

    if glucose >= 126:
        return {
            "points": 4,
            "level": "high",
            "reason": "Glucose level is in a high range."
        }

    elif glucose >= 100:
        return {
            "points": 2,
            "level": "moderate",
            "reason": "Glucose level is above the normal fasting range."
        }

    else:
        return {
            "points": 0,
            "level": "low",
            "reason": "Glucose level is within the lower-risk range."
        }


def assess_bmi(bmi):
    """
    Assess risk based on BMI.
    """

    if bmi >= 30:
        return {
            "points": 3,
            "level": "high",
            "reason": "BMI is in the obesity range."
        }

    elif bmi >= 25:
        return {
            "points": 2,
            "level": "moderate",
            "reason": "BMI is above the healthy range."
        }

    else:
        return {
            "points": 0,
            "level": "low",
            "reason": "BMI is below the higher-risk thresholds."
        }


def assess_blood_pressure(blood_pressure):
    """
    Assess risk based on blood pressure.
    """

    if blood_pressure >= 140:
        return {
            "points": 2,
            "level": "high",
            "reason": "Blood pressure is elevated."
        }

    elif blood_pressure >= 130:
        return {
            "points": 1,
            "level": "moderate",
            "reason": "Blood pressure is above the preferred range."
        }

    else:
        return {
            "points": 0,
            "level": "low",
            "reason": "Blood pressure is below the higher-risk thresholds."
        }


def assess_age(age):
    """
    Assess risk based on age.
    """

    if age >= 45:
        return {
            "points": 2,
            "level": "moderate",
            "reason": "Age is associated with increased type 2 diabetes risk."
        }

    else:
        return {
            "points": 0,
            "level": "low",
            "reason": "Age is below the higher-risk age threshold."
        }


def assess_family_history(family_history):
    """
    Assess risk based on family history.
    """

    if family_history == "Yes":
        return {
            "points": 2,
            "level": "moderate",
            "reason": "A family history of diabetes is present."
        }

    else:
        return {
            "points": 0,
            "level": "low",
            "reason": "No family history of diabetes was reported."
        }


def assess_physical_activity(activity):
    """
    Assess risk based on physical activity.
    """

    if activity == "Low":
        return {
            "points": 2,
            "level": "moderate",
            "reason": "Low physical activity may increase diabetes risk."
        }

    elif activity == "Moderate":
        return {
            "points": 1,
            "level": "low",
            "reason": "Moderate physical activity was reported."
        }

    else:
        return {
            "points": 0,
            "level": "low",
            "reason": "Regular physical activity was reported."
        }