# Basic FastAPI Server

Important things to keep in mind regarding FAST API are:
fastapi package
uvicorn
Pydantic

It works totally on decorators.

## 1) Setup (Windows)
1. Create venv:
   ```powershell
   python -m venv venv
   ```
2. Activate venv:
   ```powershell
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```powershell
   pip install fastapi uvicorn python-dotenv pydantic
   ```
4. Freeze requirements:
   ```powershell
   pip freeze > requirements.txt
   ```

## 2) Dependency Purpose
| Package | Purpose |
|---|---|
| `fastapi` | Web framework for API endpoints |
| `uvicorn` | ASGI server to run FastAPI app |
| `pydantic` | Pydantic handles validation, structure and type safety |


## 3) Project Structure (Backend)
```
backend/
  ├─ .env                # local secrets (never commit)
  ├─ .gitignore          # ignores for Python backend
  ├─ main.py             # FastAPI app startup
```

## 4) Quick Run
```powershell
cd backend
venv\Scripts\activate
uvicorn main:app --reload
```
For Swagger UI API testing:
http://127.0.0.1:8000/docs