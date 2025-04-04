FROM python:3.11-slim
WORKDIR /app
COPY . .
COPY config/ config/
RUN echo "📦 Installing requirements..." && \
    pip install --no-cache-dir -r requirements.txt && \
    echo "✅ Requirements installed."
CMD ["python", "app.py"]


