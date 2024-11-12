
<p align="center">
  <h1 align="center">SentIA: Emotional AI Counselor for Mental Health Monitoring</h1>
  <p align="center">
    <img src="./static/image.png" alt="SentIA Framework" width="800">
  </p>
</p>

## Overview

SentIA is an AI-powered emotional counselor designed to monitor and analyze users' mental health through audio input. By leveraging advanced natural language processing and sentiment analysis techniques, SentIA can detect and respond to emotional cues, providing feedback and recommendations tailored to the user’s mental state. This backend repository provides essential routes and utilities for audio processing, emotion classification, and history tracking, enabling SentIA to maintain a continuous, personalized emotional support experience.

## Features

- **Audio Processing:** Captures and processes audio input for sentiment analysis and classification.
- **Emotion Classification:** Analyzes audio transcriptions to classify emotions, using a pre-trained model.
- **User History Tracking:** Stores and retrieves user interactions to maintain context and improve response personalization.
- **Firebase Integration:** Provides real-time storage and retrieval of user data, with Firebase support for history tracking.

## Repository Structure

The codebase is organized into multiple directories and files, each contributing to the SentIA backend's functionality:

- **`app/`**: Core application logic.
  - **`routes/`**: Defines API endpoints for various services.
    - `audio.py`: Handles audio input and processing.
    - `auth.py`: Manages authentication.
    - `history.py`: Manages user history routes.
  - **`services/`**: Integration services, such as Firebase.
    - `firebase.py`: Firebase integration for data storage and retrieval.
  - **`utils/`**: Utility functions for data manipulation and model inference.
    - `prompts.py`: Defines prompt-based responses.
    - `predict_mechanism.py`: Supports emotion prediction mechanisms.
  
- **`data/`**: Directory to store dataset files and user data.

- **`static/`**: Contains static assets, such as images used in documentation.

- **Root Files**:
  - `main.py`: Main entry point for the FastAPI application.
  - `requirements.txt`: Python dependencies.
  - `README.md`: Project documentation.
  - `target_encoder.joblib`: Encodes target classes for model inference.
  - `railway.json`: Deployment configuration for Railway.app.

Each directory and file is structured to ensure modularity and clarity, making it easy to extend and maintain the codebase.

## Installation

To set up the environment for running the backend, follow these steps:

```bash
git clone https://github.com/Factral/sentia-backend-public.git
cd sentia-backend-public
pip install -r requirements.txt
```

## Usage

### Running the API

1. **Start the Server**: Run the following command to start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
2. **Access API Documentation**: Once the server is running, open your browser and go to:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Key API Endpoints

- **Audio Upload and Processing** (`/upload-audio`): Upload audio for processing and sentiment analysis.
- **User History Management** (`/add-history`, `/get-history/{username}`): Adds new entries to user history or retrieves history by username.
- **Emotion Classification** (`/classify-feelings`): Classifies emotions based on processed text.

### Firebase Setup

To enable Firebase integration for user history tracking, update the Firebase configuration in `firebase.py` with your Firebase credentials.

### Example Usage

#### Adding a New History Entry
To add a new entry to a user's history, make a `POST` request to `/add-history` with the following JSON payload:

```json
{
    "username": "fabiou",
    "date": "2024-11-13",
    "transcript": "I feel a bit anxious today.",
    "sentiment": "negative"
}
```
