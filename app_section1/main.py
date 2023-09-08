# from __future__ import annotations
import sys
sys.path.append('D:\\Soft_project')
from fastapi import FastAPI
from app.routes.user import create_user_router
from app.exception_handler import add_exception_handlers

def create_application() -> FastAPI:

    user_router = create_user_router()
    appi = FastAPI()
    appi.include_router(user_router) # Inclued the router to the app.
    add_exception_handlers(appi)

    return appi

appi = create_application()
