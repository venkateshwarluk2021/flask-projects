# use lightweight python image
FROM python:3.10-slim

# set working directory
WORKDIR /app

# copy project files
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# expose flask port
EXPOSE 5000

# run the app
CMD ["python", "flask_bmi_app.py"]


