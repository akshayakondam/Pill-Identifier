# Pill Identifier 💊

## Overview
Pill Identifier is an AI-based project designed to improve medication safety by identifying pills using visual characteristics and providing relevant drug information. The project demonstrates an end-to-end AI workflow suitable for healthcare-related use cases.

---

## Problem Statement
Medication errors can occur when pills are misidentified. This project aims to reduce such risks by using image-based classification and structured drug information retrieval.

---

## Solution Description
- Synthetic pill images are generated programmatically using Python to simulate different pill shapes and colors.
- A Convolutional Neural Network (CNN) pipeline is used to process pill images and demonstrate image classification.
- Drug information such as usage and dosage is stored in a structured CSV file and retrieved after identification (RAG-style retrieval).
- A text-to-speech module is integrated to read out pill details, improving accessibility.

---

## Tech Stack
- Python  
- TensorFlow / Keras  
- Pandas  
- Pillow (PIL)  
- pyttsx3 (Text-to-Speech)  
- Git & GitHub  

---

## Project Structure
Pill-Identifier/
├── data/
│ └── raw/ # Synthetic pill images
├── generate_pill_images.py # Dataset generation script
├── pill_identifier.py # Main AI pipeline
├── pill_info.csv # Drug information dataset
├── README.md

---

## How to Run
1. Install dependencies:
```bash
pip install tensorflow pandas pillow pyttsx3
--
2. Generate synthetic pill images:
python generate_pill_images.py
--
3.Run the pill identifier:
python pill_identifier.py
--
Author
Akshaya Kondam
AI & Data Science Enthusiast
