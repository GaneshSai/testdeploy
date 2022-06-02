import uvicorn
from fastapi import FastAPI
from utils import hello

# defining the main app
app = FastAPI(title="api", docs_url="/")


# Route definitions
@app.get("/ping")
def ping():
    return {"ping": "pong"}


@app.get("/hello/{name}", status_code=200)
def say_hello(name):
    output = {"message": hello(name)}
    return output

# Main function to start the app when main.py is called
if __name__ == "__main__":
    # Uvicorn is used to run the server and listen for incoming API requests on 0.0.0.0:8888
    uvicorn.run("main:app", host="0.0.0.0", port=9999, reload=True)
