# Plant Disease Classification and Diagnosis

## Overview
This project is a plant disease classification and diagnosis system that uses a neural network to classify plant disease images. It utilizes the Plant Village dataset for training and offers two backend options: Django and FastAPI. Additionally, a Flutter app is provided for users to upload images of plant leaves and identify the disease.

## Contents

- [Overview](#overview)
- [Features](#features)
- [Demo Video](#demo-video)
- [Installation](#installation)
  - [Backend Setup](#backend-setup)
    - [FastAPI](#fastapi)
    - [Django](#django)
  - [Flutter App](#flutter-app)
- [Usage](#usage)

## Features
- Neural network for plant disease classification.
- Used Transfer Learning using kerras model EfficientNetB3.
- Model Accuracy: approx 97.8%
- Model Size: 71 MB
- Choice of Django and FastAPI backends for serving the classification model.
- A Flutter app for users to diagnose plant diseases with uploaded leaf images.
- Easy setup and deployment with clear instructions.

## Demo Video
https://github.com/KumarUtsav1025/PlantDisClfFullStackApp/assets/92930638/27d8bdea-e215-4120-b506-a0b6f23d8c9a

## Installation

### Backend Setup

#### FastAPI
To set up the FastAPI backend, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/KumarUtsav1025/PlantDisClfFullStackApp.git
   
2. Navigate to the FastAPI backend directory:
   ```bash
    cd FastApiBackend
   
3. Create a virtual environment (optional but recommended):
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

5. Run the FastAPI backend:
   ```bash
    uvicorn main:app --reload


#### Django
To set up the Django backend, follow these steps:
1. Clone this repository:
   ```bash
   git clone https://github.com/KumarUtsav1025/PlantDisClfFullStackApp.git
   
2. Navigate to the Django backend directory:
   ```bash
   cd PlantDiseaseClassificationApp
   cd DjangoBackend
   
3. Create a virtual environment (optional but recommended):
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

5. Apply migrations and start the Django server:
   ```bash
    python manage.py migrate
    python manage.py runserver

### Flutter App
To set up the Flutter app, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/KumarUtsav1025/PlantDisClfFullStackApp.git

2. Navigate to the Flutter app directory:
    ```bash
    cd FlutterApp
    cd plant_dis_clf_app

3. Get dependecies
   ```bash
   flutter pub get
5.  Build and run the app on your preferred platform using Flutter commands:
    ```bash
    flutter run
    
## Usage
Access the FastAPI backend at http://localhost:8000 or the Django backend at http://localhost:8000 (if you set up the Django backend).
Use the Flutter app to upload plant leaf images for disease diagnosis.




