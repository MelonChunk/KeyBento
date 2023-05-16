# Use the official Python image as the base
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend code
COPY . .

# Expose the port on which the FastAPI app will run (e.g., 8001)
EXPOSE 8001

# Start the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
