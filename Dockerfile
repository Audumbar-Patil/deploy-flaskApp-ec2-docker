#   Base Image 
#   Uses a lightweight version of Python 3.11 as the base.
#   Slim version reduces image size for faster builds and less disk usage.
FROM python:3.11-slim

#   Set Working DIR 
#   Sets /app as the working directory inside the container.
WORKDIR /app

#   Copies your requirements.txt file into the container’s /app directory.
COPY requirements.txt .
#Installs the packages listed in requirements.txt using pip.
RUN pip install -r requirements.txt
#Copies all files from your project directory into the container’s /app.
COPY . .

#Sets the default command to run when the container starts — here, it runs your Flask app.
CMD ["python", "app.py"]
