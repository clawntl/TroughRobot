from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Serve the /static path
app.mount("/static", StaticFiles(directory="static"), name="static")

# Root route serves the front-end page
@app.get("/")
async def read_index():
    return FileResponse("static/index.html")

# Example API endpoint
@app.get("/api/hello")
async def hello():
    return {"message": "Hello from FastAPI on Raspberry Pi 5!"}