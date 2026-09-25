from PIL import Image
import numpy as np

def analyze_workout_image(uploaded_file, exercise):
    """Lightweight MVP image analysis. MediaPipe pose estimation can replace this function later."""
    try:
        image = Image.open(uploaded_file).convert("RGB")
        arr = np.asarray(image)
        brightness = float(arr.mean())
        # Demo score based on image quality/visibility, not a medical or biomechanical judgment.
        score = 80
        if image.width < 400 or image.height < 400:
            score -= 10
        if brightness < 45 or brightness > 240:
            score -= 5
        return {
            "score": max(0, min(100, score)),
            "summary": f"{exercise} image received successfully. For accurate joint-angle and rep detection, connect a MediaPipe/OpenPose pipeline."
        }
    except Exception:
        return {"score": 0, "summary": "The uploaded image could not be processed."}

def get_exercise_tips(exercise):
    tips = {
        "Squat": [
            "Keep the movement controlled.",
            "Keep your feet stable and knees tracking in line with your feet.",
            "Use a comfortable range of motion."
        ],
        "Push-up": [
            "Keep your body controlled as one unit.",
            "Keep hands stable and avoid rushing repetitions.",
            "Use an easier variation if needed."
        ],
        "Lunge": [
            "Take a stable step and control the movement.",
            "Keep your balance and avoid rushing.",
            "Use a comfortable depth."
        ],
        "Plank": [
            "Keep your body controlled and avoid holding your breath.",
            "Keep shoulders relaxed.",
            "Stop if you feel pain or unusual discomfort."
        ],
    }
    return tips.get(exercise, [])
