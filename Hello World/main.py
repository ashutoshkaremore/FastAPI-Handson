from fastapi import FastAPI

app = FastAPI()

@app.get('/test')

def test():
    return {"message": "Hello, World!"}