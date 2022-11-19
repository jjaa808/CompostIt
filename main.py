from fastapi import FastAPI, Path
from starlette.responses import FileResponse
app = FastAPI()

@app.get("/")
def home():
    return "Compost It"

@app.get("/contact")
def contact():
    return FileResponse("vievs/main_page.html")

@app.get("/about")
def about():
    return FileResponse("vievs/about.html")