from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "ola, mundo! sou o teste de re-build"}
