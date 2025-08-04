# AI-Powered Email Reply Generator

This Streamlit app generates context-aware email replies using DeepSeek R1 via OpenRouter API. Users can paste an email, select the reply tone, describe the intent, and get an editable AI-generated response. Feedback (rating and suggestions) is stored in a CSV file.

## Features
- Paste received email
- Select reply tone (Formal, Friendly, Assertive)
- Describe intended reply message
- Generate reply using DeepSeek R1 (OpenRouter API)
- Editable AI output
- Feedback form (rating & suggestions)
- Feedback stored in CSV
- Robust error handling
- Modular architecture

## Setup
1. **Set your OpenRouter API key**: Pass it as an environment variable `OPENROUTER_API_KEY`.
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app**:
   ```bash
   streamlit run app/main.py
   ```

## Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t email-reply-generator .
   ```
2. Run the container (set your API key):
   ```bash
   docker run -e OPENROUTER_API_KEY=your_api_key -p 8501:8501 email-reply-generator
   ```

## Render Deployment
- Use the Dockerfile and set `OPENROUTER_API_KEY` in Render's environment settings.

## File Structure
- `app/ui.py`: Streamlit UI components
- `app/api_handler.py`: OpenRouter API logic
- `app/reply_generator.py`: Reply generation logic
- `app/feedback_manager.py`: Feedback CSV management
- `app/main.py`: App entry point
- `requirements.txt`: Python dependencies
- `Dockerfile`: Containerization
- `README.md`: Documentation
