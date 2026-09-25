import streamlit as st
from pathlib import Path
from datetime import datetime
import pandas as pd

from modules.workout import analyze_workout_image, get_exercise_tips
from modules.diet import nutrition_guidance
from modules.habits import habit_score, habit_message
from modules.chatbot import gym_buddy_response
from modules.recommender import recommend_workouts

st.set_page_config(page_title="AI Gym & Fitness Assistant", page_icon="🏋️", layout="wide")

st.title("🏋️ AI Gym & Fitness Assistant")
st.caption("A modular AI fitness ecosystem — trainer, nutrition guide, habit tracker and virtual gym buddy.")

if "workouts" not in st.session_state:
    st.session_state.workouts = []
if "habits" not in st.session_state:
    st.session_state.habits = {"workout": False, "water": False, "sleep": False, "meal": False}

with st.sidebar:
    st.header("👤 Profile")
    name = st.text_input("Name", "User")
    goal = st.selectbox("Primary goal", ["General fitness", "Strength", "Endurance", "Mobility"])
    experience = st.selectbox("Experience", ["Beginner", "Intermediate", "Advanced"])
    st.divider()
    st.info("This MVP provides general fitness guidance and is not a medical diagnosis or treatment tool.")

tabs = st.tabs([
    "🏠 Dashboard", "🏋️ AI Gym Trainer", "🥗 Nutrition Coach",
    "📈 Habit Tracker", "🤖 Gym Buddy", "🧠 Planner"
])

with tabs[0]:
    st.subheader(f"Welcome, {name} 👋")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Workout sessions", len(st.session_state.workouts))
    c2.metric("Habit score", f"{habit_score(st.session_state.habits)}%")
    c3.metric("Goal", goal)
    c4.metric("Level", experience)
    st.markdown("### Project modules")
    st.write("Workout detection • Nutrition guidance • Habit tracking • Conversational assistant • Workout planner")
    st.success("Start with the AI Gym Trainer tab to test the first module.")

with tabs[1]:
    st.subheader("AI Gym Trainer")
    st.write("Upload a workout image. The MVP analyzes the image and gives exercise-form guidance. Video/real-time pose detection can be added as the next phase.")
    uploaded = st.file_uploader("Upload workout image", type=["jpg", "jpeg", "png"])
    exercise = st.selectbox("Exercise", ["Squat", "Push-up", "Lunge", "Plank"])
    if uploaded:
        st.image(uploaded, caption="Uploaded workout image", use_container_width=True)
        result = analyze_workout_image(uploaded, exercise)
        st.markdown(f"**Analysis:** {result['summary']}")
        st.metric("Demo performance score", f"{result['score']}/100")
        st.markdown("**Form checklist**")
        for tip in get_exercise_tips(exercise):
            st.write("•", tip)
        if st.button("Add workout session"):
            st.session_state.workouts.append({
                "date": datetime.now().strftime("%Y-%m-%d"),
                "exercise": exercise,
                "score": result["score"]
            })
            st.success("Workout session added.")

with tabs[2]:
    st.subheader("🥗 AI Dietician & Nutrition Coach")
    st.write("General nutrition guidance based on your selected goal and preferences.")
    preference = st.selectbox("Diet preference", ["Balanced", "Vegetarian", "Vegan", "High-protein"])
    meals = nutrition_guidance(goal, preference)
    for meal, items in meals.items():
        st.markdown(f"**{meal}**")
        st.write(" • ".join(items))
    st.caption("For medical conditions, allergies, eating concerns, or individualized nutrition plans, consult a qualified professional.")

with tabs[3]:
    st.subheader("📈 AI Fitness Habit Tracker")
    for key, label in [
        ("workout", "Completed today's workout"),
        ("water", "Stayed hydrated"),
        ("sleep", "Got adequate rest"),
        ("meal", "Had balanced meals"),
    ]:
        st.session_state.habits[key] = st.checkbox(label, value=st.session_state.habits[key])
    score = habit_score(st.session_state.habits)
    st.progress(score / 100)
    st.metric("Today's habit score", f"{score}%")
    st.info(habit_message(score))

with tabs[4]:
    st.subheader("🤖 Virtual Gym Buddy")
    for q in [
        "Give me a short workout motivation message.",
        "How should I approach a beginner workout?",
        "I missed my planned workout. What should I do?"
    ]:
        if st.button(q):
            st.write(gym_buddy_response(q))
    custom = st.text_input("Ask your gym buddy")
    if custom:
        st.write(gym_buddy_response(custom))

with tabs[5]:
    st.subheader("🧠 Gym Recommender & Planner")
    days = st.slider("Days available this week", 2, 7, 4)
    plan = recommend_workouts(goal, experience, days)
    st.dataframe(pd.DataFrame(plan), use_container_width=True, hide_index=True)

    st.markdown("### Workout history")
    if st.session_state.workouts:
        st.dataframe(pd.DataFrame(st.session_state.workouts), use_container_width=True, hide_index=True)
    else:
        st.caption("No workout sessions recorded yet.")
