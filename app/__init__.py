from fastapi import FastAPI
from uvicorn import run as run_uvicorn
from .db import AsyncDB


app = FastAPI(debug=True)


from . import routes


def main() -> None:
    AsyncDB.migrate()
    run_uvicorn(app=app, port=8000)