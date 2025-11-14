## 📄 README.md Template

```markdown
# Overtone Recommendation Service (FastAPI & MongoDB Atlas)

This is a **Python FastAPI microservice** designed to provide music recommendations. It utilizes an asynchronous driver (**Motor**) to connect to **MongoDB Atlas** and is containerized using **Docker** for cloud deployment on **Render**.

This project was completed as part of **Assignment 4: Deploying a FastAPI Application with MongoDB Atlas and Render**.

---

## 🚀 Deployment Status

| Service | Status | Live URL |
| :--- | :--- | :--- |
| **Recommendation Service** | **Deployed** | `https://dashboard.render.com/web/srv-d4bg4abuibrs739s6lgg/logs` |
| **Health Endpoint** | **Working** | `https://dashboard.render.com/web/srv-d4bg4abuibrs739s6lgg/logs/health/db` |

---

## ⚙️ Technologies Used

* **Framework:** FastAPI
* **Database:** MongoDB Atlas (via **Motor** driver)
* **Containerization:** Docker
* **Cloud Platform:** Render
* **Dependencies:** `uvicorn`, `httpx`, `pydantic`

---

## 🛠️ Project Structure

The core logic is contained within the `app/` directory:

```

.
├── app/
│   ├── database.py         \# MongoDB connection setup & environment variable handling.
│   ├── main.py             \# FastAPI entry point, middleware, and router registration.
│   ├── models.py           \# Pydantic schemas for data validation.
│   ├── routes/
│   │   ├── health.py       \# **CRITICAL:** Implements the /health/db endpoint.
│   │   └── recommendations.py \# Main recommendation routes.
│   └── utils/
│       └── logic.py        \# Business logic (e.g., calling the fake review service).
├── Dockerfile              \# Instructions for building the service image.
├── requirements.txt        \# Python dependencies.
└── README.md

````

---

## 🌍 Environment Configuration

The application requires the following environment variables to be set securely in the **Render Dashboard**. They are read by `app/database.py` and are **not** committed to the repository.

| Variable Name | Description |
| :--- | :--- |
| `MONGO_URI` | The full connection string from MongoDB Atlas. |
| `DB_NAME` | The target database name (e.g., `assignmentdb`). |
| `JWT_SECRET` | A secure, random secret key for token signing (required by the assignment). |

---

## 🐳 Docker Deployment & SSL/TLS Solution

### Dockerfile Key Feature

To successfully connect to MongoDB Atlas from the Render container, which uses SSL/TLS encryption, a critical step was implemented in the `Dockerfile`:

```dockerfile
# CRITICAL STEP: Installing system certificates for MongoDB Atlas SSL/TLS
RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates openssl && \
    update-ca-certificates && \
    rm -rf /var/lib/apt/lists/*
````

This command ensures the necessary **system certificates (`ca-certificates`, `openssl`)** are available inside the `python:3.11-slim` container, preventing common SSL connection errors during deployment.

### Render Setup

1.  **Create a Web Service** on Render.
2.  Select **Docker** as the deployment method.
3.  Set the **Environment Variables** (listed above) in the dashboard.

-----

## 💡 Key Endpoints

| Method | Endpoint | Description | Verification Criteria |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Basic health check. | Service is running. |
| `GET` | `/health/db` | **Mandatory Check.** Verifies active connectivity to MongoDB Atlas. | Must return `{"status": "ok", ...}` with HTTP 200. |
| `GET` | `/recommendations/{user_id}` | Fetches recommendations based on user reviews (uses fake review service logic). | Service logic is functional. |

```
```
