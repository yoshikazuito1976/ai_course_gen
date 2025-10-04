from fastapi import FastAPI
from .schemas import OutlineIn, OutlineOut
from .service import generate_outline

app = FastAPI(title="AI Course Generator")

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is running!"}


@app.post("/outline", response_model=OutlineOut)
def outline(body: OutlineIn):
    data = generate_outline(body.topic, body.grade)
    return {"ok": True, "data": data}
