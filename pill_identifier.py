import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import pyttsx3
import os

# Voice output
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Load pill info
pill_info = pd.read_csv("pill_info.csv")

# Labels derived from image naming
labels = pill_info["pill_name"].tolist()

# Simple CNN model (demo)
model = Sequential([
    Conv2D(8, (3,3), activation="relu", input_shape=(128,128,3)),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(16, activation="relu"),
    Dense(len(labels), activation="softmax")
])

model.compile(optimizer="adam", loss="categorical_crossentropy")

def predict_pill(image_path):
    img = load_img(image_path, target_size=(128,128))
    img = img_to_array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    # Dummy prediction (for demo purposes)
    pill_name = labels[0]

    info = pill_info[pill_info["pill_name"] == pill_name].iloc[0]
    result = f"Pill: {pill_name}, Uses: {info['uses']}, Dosage: {info['dosage']}"
    print(result)
    speak(result)

# Example
predict_pill("data/raw/round_red_1.png")
