FROM python:3.13-slim-bookworm

WORKDIR /app

RUN apt-get update && apt-get upgrade -y

# Install tkinter (it's usually included but let's be explicit)
RUN apt-get install -y --no-install-recommends tk

# Install nltk
RUN pip install --no-cache-dir nltk

# Download the entire nltk_data
RUN python -m nltk.downloader -d /usr/local/nltk_data all

# Set the NLTK_DATA environment variable
ENV NLTK_DATA=/usr/local/nltk_data

# Copy your application code
COPY . .

# Set the command to run your script
CMD ["python", "text_summarizer.py"]