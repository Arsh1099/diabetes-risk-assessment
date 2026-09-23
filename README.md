# AI-Based Diabetes Risk Assessment

## CODETECH Artificial Intelligence Internship Project

### Project Overview

This project is an educational Artificial Intelligence expert system designed to assess diabetes risk using a knowledge base and rule-based reasoning.

Instead of training a machine learning model, the system uses predefined domain rules and an inference engine to analyze user-provided information.

The application provides:

- Risk assessment
- Risk factors identified
- Triggered rules
- Explanation of the reasoning process
- General health guidance

---

## Domain

Artificial Intelligence

## Internship Organization

CODETECH

## Project Type

Knowledge-Based AI Expert System

---

## How the System Works

The system follows this process:

User Input  
↓  
Knowledge Base  
↓  
Rule Evaluation  
↓  
Inference Engine  
↓  
Risk Assessment  
↓  
Explanation

---

## AI Components

### 1. Knowledge Base

The knowledge base stores the rules used by the system.

Examples include rules related to:

- Fasting glucose
- BMI
- Blood pressure
- Age
- Family history
- Physical activity

### 2. Inference Engine

The inference engine evaluates the user's information against the rules in the knowledge base.

### 3. Rule-Based Reasoning

The system identifies which rules are triggered and combines their results to determine an overall assessment.

### 4. Explainable Output

The application explains which factors and rules contributed to the result.

---

## Technologies Used

- Python
- Streamlit
- Visual Studio Code
- Git
- GitHub

---

## Project Structure

```text
diabetes-risk-assessment/
│
├── ai_engine/
│   ├── __init__.py
│   └── inference_engine.py
│
├── knowledge_base/
│   ├── __init__.py
│   └── diabetes_rules.py
│
├── screenshots/
│
├── app.py
├── test_ai.py
├── requirements.txt
├── README.md
└── .gitignoregit