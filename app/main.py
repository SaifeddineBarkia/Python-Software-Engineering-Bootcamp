# from __future__ import annotations
import os
import sys

current_path = os.getcwd()
current_path = "\\".join(current_path.split('\\')[:-1])

sys.path.append(current_path)
from fastapi import FastAPI
from app.routes.user import create_user_router
from app.exception_handler import add_exception_handlers

def create_application() -> FastAPI:
    profile_infos, users_content = create_profile_infos_and_users_content()
    user_router = create_user_router(profile_infos,users_content)
    appi = FastAPI()
    appi.include_router(user_router) # Inclued the router to the app.
    add_exception_handlers(appi)

    return appi


def create_profile_infos_and_users_content():

    users_content = {
        0: {
            "name": "A",
            "liked_posts": [1,2,3],
        }
    }
    profile_infos = {
        0:{
            "short_description":"This is short",
            "long_bio": "This longer"
        }
    }

    return profile_infos, users_content

appi = create_application()
