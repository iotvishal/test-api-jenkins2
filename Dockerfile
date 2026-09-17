FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml .
COPY requirements.txt .
COPY src ./src
RUN pip install --no-cache-dir -e .
EXPOSE 5000
CMD ["python", "-m", "task_api.main"]