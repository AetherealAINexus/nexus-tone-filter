FROM python:3.11-slim

WORKDIR /app

# Copy everything first
COPY . .

# (Optional: Still explicitly copy config)
COPY config/ config/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the default port
EXPOSE 8080

# Start the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]