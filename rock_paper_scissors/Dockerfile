# use lightweight python image
FROM python:3.10-slim

# set working directory
WORKDIR /app

# copy files
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# exposr flask port
EXPOSE 5000

# run flask app
CMD ["python", "flask_rps_app.py"]