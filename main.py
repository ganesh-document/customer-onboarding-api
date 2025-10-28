from fastapi  FastAPI
app = FastAPI()

@app.get'/'
def root:
    return {'message': 'Hello'}
