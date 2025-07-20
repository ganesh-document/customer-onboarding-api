from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def root():
    X
    return {'message': 'Hello'}
