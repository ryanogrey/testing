from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello Test User Deployment. WE ARE GREAT"}