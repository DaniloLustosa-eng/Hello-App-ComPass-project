from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "ola, TESTANDO PULL REQUEST"}
