# Stage 1: Build Stage
FROM python:3.8-slim as builder

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install build dependencies
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the application source code
COPY . .

# Run tests and linting
RUN pip install pytest flake8 pytest-cov \
    && pytest --junitxml=reports/test-results.xml --cov=src --cov-report=xml \
    && flake8 . --exit-zero --max-line-length=88 --statistics

# Stage 2: Final Stage
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy only the necessary files from the builder stage
COPY --from=builder /app /app
COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages

# Expose port 80
EXPOSE 80

# Run the application
CMD ["python", "app.py"]
