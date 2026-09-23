"""
AI Inference Engine
-------------------

This module combines user facts with the rules stored
in the knowledge base and produces an explainable
risk assessment.

This is an educational expert system and is not a
clinically validated diagnostic tool.
"""

from knowledge_base.diabetes_rules import (
    assess_glucose,
    assess_bmi,
    assess_blood_pressure,
    assess_age,
    assess_family_history,
    assess_physical_activity
)


def assess_diabetes_risk(
    age,
    glucose,
    bmi,
    blood_pressure,
    family_history,
    physical_activity
):
    """
    Evaluate the supplied facts using the knowledge base.

    Returns:
        dict containing:
        - risk_level
        - score
        - reasons
        - triggered_rules
    """

    # --------------------------------------------------
    # 1. Evaluate individual rules
    # --------------------------------------------------

    rule_results = {
        "Glucose Rule": assess_glucose(glucose),
        "BMI Rule": assess_bmi(bmi),
        "Blood Pressure Rule": assess_blood_pressure(blood_pressure),
        "Age Rule": assess_age(age),
        "Family History Rule": assess_family_history(family_history),
        "Physical Activity Rule": assess_physical_activity(
            physical_activity
        )
    }


    # --------------------------------------------------
    # 2. Calculate total score
    # --------------------------------------------------

    total_score = sum(
        result["points"]
        for result in rule_results.values()
    )


    # --------------------------------------------------
    # 3. Find triggered rules
    # --------------------------------------------------

    triggered_rules = []

    for rule_name, result in rule_results.items():

        if result["points"] > 0:

            triggered_rules.append({
                "rule": rule_name,
                "level": result["level"],
                "points": result["points"],
                "reason": result["reason"]
            })


    # --------------------------------------------------
    # 4. Count important factors
    # --------------------------------------------------

    high_factors = sum(
        1
        for result in rule_results.values()
        if result["level"] == "high"
    )

    moderate_factors = sum(
        1
        for result in rule_results.values()
        if result["level"] == "moderate"
    )


    # --------------------------------------------------
    # 5. Inference logic
    # --------------------------------------------------

    # A strong glucose signal is treated as an important
    # rule trigger in this educational system.
    if glucose >= 126:

        risk_level = "HIGH RISK"


    # Multiple high/moderate factors together
    elif high_factors >= 2:

        risk_level = "HIGH RISK"


    elif high_factors == 1 and moderate_factors >= 2:

        risk_level = "HIGH RISK"


    # Several moderate risk factors
    elif moderate_factors >= 3:

        risk_level = "MODERATE RISK"


    # One meaningful risk factor
    elif high_factors == 1 or moderate_factors >= 1:

        risk_level = "MODERATE RISK"


    else:

        risk_level = "LOW RISK"


    # --------------------------------------------------
    # 6. Explanation generation
    # --------------------------------------------------

    reasons = [
        item["reason"]
        for item in triggered_rules
    ]


    if not reasons:

        reasons.append(
            "No major higher-risk factors were identified "
            "by the current rule set."
        )


    # --------------------------------------------------
    # 7. Return complete result
    # --------------------------------------------------

    return {
        "risk_level": risk_level,
        "score": total_score,
        "reasons": reasons,
        "triggered_rules": triggered_rules
    }