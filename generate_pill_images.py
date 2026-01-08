from PIL import Image, ImageDraw
import os
import random

OUTPUT_DIR = "data/raw"
os.makedirs(OUTPUT_DIR, exist_ok=True)

shapes = ["round", "oval", "capsule"]
colors = ["white", "red", "blue", "yellow"]

def create_pill(shape, color, idx):
    img = Image.new("RGB", (128, 128), "black")
    draw = ImageDraw.Draw(img)

    if shape == "round":
        draw.ellipse((32, 32, 96, 96), fill=color)
    elif shape == "oval":
        draw.ellipse((20, 40, 108, 88), fill=color)
    else:  # capsule
        draw.rectangle((32, 48, 96, 80), fill=color)

    filename = f"{shape}_{color}_{idx}.png"
    img.save(os.path.join(OUTPUT_DIR, filename))

for i in range(200):
    create_pill(random.choice(shapes), random.choice(colors), i)

print("Pill images generated successfully!")
