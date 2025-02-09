# BA_DCS_lastsemmaxxing

## Key Resources
Weekly Updates: https://drive.google.com/drive/folders/1o8y0EWdAuGMQe17fiuy6eFUvAWo5dUt3?usp=drive_link

## Installation
### Backend:
1. Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2. Create a virtual environment:
    ```bash
    python -m venv env
    ```
3. Activate the virtual environment:
    - On Windows:
      ```bash
      env\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source env/bin/activate
      ```
4. Install required packages:
    ```bash
    pip install flask flask-cors ocrmypdf pypdf python-docx
    ```

### Frontend:
1. Navigate to the frontend project directory:
    ```bash
    cd frontend/my-app
    ```
2. Install dependencies (if not already installed):
    ```bash
    npm install
    ```

## Running the Application

### Backend:
1. Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2. Create and activate the virtual environment (if not already done):
    ```bash
    python -m venv env
    env\Scripts\activate  # For Windows
    # OR
    source env/bin/activate  # For macOS/Linux
    ```
3. Start the backend server:
    ```bash
    python app.py
    ```
4. Open the backend in your browser or API client at:
    ```
    http://127.0.0.1:5000
    ```

### Frontend:
1. Navigate to the `frontend/my-app` directory:
    ```bash
    cd frontend/my-app
    ```
2. Start the development server:
    ```bash
    npm run dev
    ```
3. Open the application in your browser at:
    ```
    http://localhost:3000
    ```
## Env Files:
### Frontend:
1. frontend/my-app/.env:
    ```
    NEXT_PUBLIC_BACKEND_API_URL (URL to backend)
    ```
