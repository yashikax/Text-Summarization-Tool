# Text-Summarization-Tool

## Overview

A simple Text Summarization Tool with a GUI built using `tkinter` and `nltk` for extractive summarization. Allows pasting text, uploading `.txt` files, and adjusting summary length. Containerized with Docker and built using Windsurf.

## Features

* Paste or upload text for summarization.
* Basic extractive summarization using `nltk`.
* Adjustable summary length via a slider.
* Dockerized for easy setup.

## Technologies

* Python 3
* tkinter
* nltk
* Docker

## Setup (Docker)

1.  Install Docker.
2.  Clone this repo.
3.  Build: `docker build -t text-summarizer-app .`
4.  (for Windows, ensure VcXsrv is running with display `0` and access control disabled):
5.  Run (Windows): `docker run -it --rm -e DISPLAY=host.docker.internal:0 -v /tmp/.X11-unix:/tmp/.X11-unix text-summarizer-app`
6.  Run (Linux/macOS): `docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix text-summarizer-app`

## Usage

1.  Run the Docker container.
2.  Use the GUI to input text or upload a file.
3.  Adjust the summary length slider.
4.  Click "Summarize".

## Windsurf Usage

Windsurf aided in GUI generation, summarization logic, file upload, slider implementation, and Dockerfile creation. It also helped resolve library issues and NLTK data dependencies.
