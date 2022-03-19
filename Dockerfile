# This Dockerfile is from https://github.com/thedirtyfew/dash-docker-mwe

FROM python:3.8-slim-buster

# Create a working directory.
RUN mkdir /app
WORKDIR /app

# Install Python dependencies.
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the rest of the codebase into the image
COPY . ./

# Finally, run gunicorn.
CMD [ "gunicorn", "--workers=5", "--threads=1", "-b 0.0.0.0:8000", "src.app:server"]
