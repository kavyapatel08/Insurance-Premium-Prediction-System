#  Base Image
FROM python:3.11-slim

#  Set working directory
WORKDIR /app

#  Copy dependency files
COPY requirements.txt .

#  Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#  Copy project files into container
COPY . .

#  Expose both FastAPI (8000) and Streamlit (8501)
EXPOSE 8000

# command to start FastAPI Application
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]


