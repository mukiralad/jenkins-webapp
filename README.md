# CI/CD Pipeline for Containerized Web App

## Overview

This project demonstrates how to build a Continuous Integration/Continuous Deployment (CI/CD) pipeline using Jenkins for a containerized Flask web application. The pipeline includes building, testing, and deploying the application.
Project Overview
The goal of this project is to:

Build a simple Flask web application.

Containerize the application using Docker.

Write automated unit tests using pytest.

Set up a Jenkins pipeline for CI/CD.

This project is designed to showcase skills relevant to software engineering roles, including DevOps practices, containerization, CI/CD pipelines, and observability.

## Repository Structure

- **app/**: Contains the Python application code.
- **Dockerfile**: Defines the Docker image for the web application.
- **Jenkinsfile**: Contains the Jenkins pipeline configuration.

## Prerequisites

- Docker
- Jenkins
- Python 3.x

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/mukiralad/jenkins-webapp.git
cd jenkins-webapp
```
2. Build the Docker Image:
```bash
docker build -t webapp:latest .
```
3. Run the Docker Container:
```bash
docker run -p 5000:5000 webapp:latest
```
4. Access the web application at ```http://localhost:5000```
