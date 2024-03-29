from os import environ

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import PlainTextResponse

from src.config import fastApiConfig
from src.db.mongo import MongoEngine
from src.routes import (
    configuration_routes,
    email_routes,
    root_routes,
    user_routes
)
from src.services import ErrorAPI

app = FastAPI(**fastApiConfig)
db = MongoEngine().get_connection()


@app.exception_handler(Exception)
def http_error_report(_, exc: Exception):
    ErrorAPI.report_error(str(exc), code=500)
    return PlainTextResponse("Internal Server Error", status_code=500)


app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=environ.get("ALLOWED_HOSTS", "*").split(",")
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=environ.get("ALLOW_CREDENTIALS", True),
    allow_origins=environ.get("ALLOWED_ORIGINS", "*").split(","),
    allow_methods=environ.get("ALLOWED_METHODS", "*").split(","),
    allow_headers=environ.get("ALLOWED_HEADERS", "*").split(",")
)

app.include_router(user_routes)
app.include_router(email_routes)
app.include_router(configuration_routes)
app.include_router(root_routes)
