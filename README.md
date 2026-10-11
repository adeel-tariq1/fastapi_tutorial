# FastAPI Tutorial — Python API Development

A hands-on collection of Python examples covering **FastAPI concepts, API development, and backend fundamentals**. This repository documents my learning journey through separate code examples, with each `.py` file focusing on a specific concept or implementation.

## 🎯 Objectives

* Understand how FastAPI applications are structured.
* Build REST APIs using routes, path parameters, and query parameters.
* Validate request data using Pydantic models.
* Explore middleware, exception handling, and HTTP status codes.
* Implement caching to improve API response times.
* Learn authentication, database integration, and other backend concepts through practical examples.
* Develop a strong foundation for building scalable AI-powered backend applications.

## 📚 Topics Covered

The repository includes practical examples of topics such as:

* **FastAPI Fundamentals** — Application setup, endpoints, and routing.
* **Request Parameters** — Path parameters and query parameters.
* **Data Validation** — Pydantic models and structured request data.
* **Middleware** — Processing requests and responses.
* **Error Handling** — Exceptions and HTTP responses.
* **Caching** — In-memory caching and caching libraries.
* **Authentication** — JWT and related authentication concepts.
* **Database Integration** — Working with databases and persistent data.
* **File Handling** — Uploading and serving files.
* **API Testing** — Testing endpoints and validating responses.

*Note: Topics and examples may evolve as I progress through the tutorial.*

## 🛠️ Tech Stack

* Python
* FastAPI
* Uvicorn
* Pydantic
* Supporting Python libraries used in individual examples

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/fastapi_tutorial.git
```

### 2. Navigate to the project directory

```bash
cd fastapi_tutorial
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install the required packages

Install FastAPI and Uvicorn:

```bash
python -m pip install fastapi uvicorn
```

Some examples require additional libraries. Install those as needed for the specific file you want to run.

### 5. Run an example

For a file named `main.py` containing a FastAPI application instance named `app`:

```bash
python -m uvicorn main:app --reload
```

Open the interactive API documentation at:

* **Swagger UI:** http://127.0.0.1:8000/docs
* **ReDoc:** http://127.0.0.1:8000/redoc

Replace `main:app` with the appropriate module and application names for other examples.

## 📁 Repository Structure

```text
fastapi_tutorial/
├── .gitignore
├── README.md
├── main.py
├── middleware.py
├── jwt_auth.py
├── fastapi_cache_lib.py
└── ...other Python examples
```

The filenames above are illustrative. The repository contains separate Python files for the concepts being explored.

## 💡 Learning Approach

I use this repository to practice concepts through code, understand how different FastAPI features work, and build a stronger foundation in backend development.

My broader goal is to use these backend skills to develop **AI applications, Generative AI solutions, and AI agent-based systems**.

## 📈 Progress

This is an ongoing learning repository. Examples will be improved and new concepts added as I continue learning and experimenting with FastAPI.

## 🤝 Contributions

Suggestions, feedback, and constructive discussions are welcome.

