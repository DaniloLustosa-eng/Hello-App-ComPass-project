from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "ola, mundo! teste para provar que o pull requets está funcionando!"}
