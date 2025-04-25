from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the MLOps Lab!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
