from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on Docker!"


#1. Flask App Creation
#   app = Flask(__name__) initializes a new Flask web application. __name__ tells Flask where to look for resources like templates and static files. 
#2. Defining a Route
#   @app.route('/') sets up the home route (/). This means when you visit the root URL (like http://localhost:5000), the function below it will run.
#3. Defining a View Function
#   def home(): return "Hello from Flask on Docker!" defines the function that runs when someone accesses the home page. It returns a simple string as the web page content.
#4. Web Server Behavior
#   Flask will start a lightweight development server when you run the script (usually with python app.py). The server listens for HTTP requests and routes them based on URL patterns.
#5. 
