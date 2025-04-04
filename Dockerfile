# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (separately to leverage caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the app
COPY . .

# Expose port (optional)
EXPOSE 8080

# Start the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]