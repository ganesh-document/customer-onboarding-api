from fastapi import 
app = FastAPI()

@app.get('/')
def root
    return {'message': 'Hello'}
