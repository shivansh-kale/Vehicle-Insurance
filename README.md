# Vehicle Insurance Prediction - MLOps Learning Project

##  About This Project

This repository is intended for learning MLOps concepts. The focus is understanding production workflows, Docker, CI/CD, MongoDB, AWS, and project architecture through hands-on implementation.

The implementation is based on concepts learned from an MLOps lifecycle. I studied every module, file, and function in detail, adding extensive comments throughout the project to understand **what each line does, why it exists, and how different components interact.**

> **Purpose:** Learning MLOps engineering practices.

---

#  Learning Objectives

The primary goal of this project was to gain hands-on experience with the complete MLOps workflow, including:

- End-to-End ML Pipeline
- Modular Project Structure
- Logging & Exception Handling
- MongoDB Integration
- AWS Cloud Integration
- Docker Containerization
- CI/CD using GitHub Actions
- Deployment Workflow
- Environment Variable Management
- Model Serialization
- Project Packaging
- Production-ready Code Organization

---

**During this project, I explored and understood:**

## Machine Learning

- Data Ingestion
- Data Validation
- Data Transformation
- Model Training
- Hyperparameter Tuning
- Model Evaluation
- Prediction Pipeline

---

## Software Engineering

- Clean Project Structure
- Python Packaging
- Configuration Management
- Logging
- Exception Handling
- Utility Functions
- Environment Variables
- Modular Programming

---

## Database

- MongoDB Atlas
- Reading & Writing Data
- Database Connectivity
- Data Storage Pipeline

---

## Cloud

- AWS
- IAM Users
- S3 Bucket Integration
- Authentication using Environment Variables

---

## DevOps / MLOps

- Docker
- Dockerfile
- Docker Image
- Docker Container
- GitHub Actions
- Continuous Integration
- Continuous Deployment
- Deployment Automation

---

#  Project Workflow

```
Dataset

      │

      ▼

MongoDB

      │

      ▼

Data Ingestion

      │

      ▼

Data Validation

      │

      ▼

Data Transformation

      │

      ▼

Model Training

      │

      ▼

Model Evaluation

      │

      ▼

Model Saved

      │

      ▼

Prediction Pipeline

      │

      ▼

FastAPI / Web Application

      │

      ▼

Docker Container

      │

      ▼

GitHub Actions (CI/CD)

      │

      ▼

AWS Deployment
```

---

# 📂 Project Structure

```
.
├── config/
├── logs/
├── notebook/
├── src/
├── static/
├── templates/
├── .github/workflows/
├── app.py
├── Dockerfile
├── requirements.txt
├── setup.py
├── pyproject.toml
└── README.md
```

---

# Note
This repository should be viewed as a **learning project**.

My objective was to understand:

- how an ML project is organized,
- how production pipelines are built,
- how Docker packages applications,
- how CI/CD automates deployment,
- how MongoDB and AWS integrate with ML systems,
- and how all these technologies work together in an end-to-end workflow.

To reinforce my understanding, I added detailed comments throughout the codebase explaining the purpose of classes, functions, and important implementation details.

---

# Tools and services used

- Python
- Scikit-Learn
- FastAPI
- MongoDB Atlas
- AWS
- Docker
- GitHub Actions
- HTML
- CSS

---

# Future Improvements (working on)

Some improvements I plan to implement myself:

- Add MLflow for experiment tracking
- Add DVC for dataset versioning
- Kubernetes deployment
- Monitoring using Prometheus & Grafana
- Better API documentation
- Unit & Integration Tests
- Model Registry
- Automatic Retraining Pipeline

---


# Check
If you're learning MLOps, feel free to explore this repository. The code contains detailed comments that explain not only *what* each component does, but also *why* it is needed in a production Machine Learning pipeline.
