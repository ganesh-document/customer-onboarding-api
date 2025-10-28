
app = FastAPI()

@app.get('/')
def root():
     {'message': 'Hello'}
