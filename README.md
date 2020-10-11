# tobytalks
The backend for the Google Assistant Toby Talks application.

# Requirments 

ngrok

uvicorn

fastapi

pydantic

pip install fastapi uvicorn pydantic

# Running the Python backend

Download app.py from this Git, ngrok, and uvicorn.

Run ngrok:

https://ngrok.com/download

./ngrok http 8080

Run unvicorn in the location of app.py:

uvicorn --port 8080 app:app
