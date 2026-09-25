# AI Gym & Fitness Assistant

A Streamlit MVP based on the uploaded project specification.

## Current MVP modules
1. AI Gym Trainer — image upload + exercise-specific guidance.
2. Nutrition Coach — general meal guidance based on goal and diet preference.
3. Habit Tracker — daily habit score and feedback.
4. Virtual Gym Buddy — conversational rule-based assistant.
5. Gym Recommender & Planner — weekly plan generator.

## Run locally

Use Python 3.11 or 3.12 for the easiest package compatibility.

```bash
python -m venv venv
```

Windows PowerShell:
```bash
.\venv\Scripts\Activate.ps1
```

Install:
```bash
pip install -r requirements.txt
```

Run:
```bash
streamlit run app.py
```

## Next development phase

The project specification proposes React/Next.js, Python FastAPI/Flask, TensorFlow/PyTorch/OpenCV/MediaPipe, MongoDB/PostgreSQL, MQTT/Node-RED, LLM/NLP, cloud storage and Plotly/D3.js.

The next step is to replace the lightweight workout image analyzer with a real MediaPipe/OpenPose pipeline, add persistent database storage, and connect a real conversational AI API.
