# base image
FROM python:3.11-slim

# set working directory
WORKDIR /app

# copy requirements first for caching
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt 

# copy all project files
COPY . .

# expose port
EXPOSE 5000

# run flask app
CMD ["python", "flask_library_app.py"]