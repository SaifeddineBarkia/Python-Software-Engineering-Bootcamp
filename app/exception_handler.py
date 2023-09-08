from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.exceptions import UserNotFound
import logging

logger = logging.getLogger(__name__)

def add_exception_handlers(app: FastAPI) -> None:

    @app.exception_handler(UserNotFound)
    async def hande_user_not_found_exception(request: Request, exc: UserNotFound):
        logger.error(f'None existent user_id: {exc.user_id} was requested')
        return JSONResponse(status_code=404, content="User doesn't exist")

    return None