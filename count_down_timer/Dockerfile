# Use small Python image
FROM python:3.11-slim

# Create app dir
WORKDIR /app

# Install system deps (optional but helpful for tz/locale)
RUN apt-get update && apt-get install -y --no-install-recommends \
    tzdata && rm -rf /var/lib/apt/lists/*

# Install Python deps first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

# Environment for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 5000

# Run (dev server is fine for practice)
CMD ["flask", "run", "--port=5000"]
