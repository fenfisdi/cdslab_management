from os import environ

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from src.config import fastApiConfig
from src.db.mongo import MongoEngine
from src.routes import email_routes, user_routes

app = FastAPI(**fastApiConfig)
db = MongoEngine().get_connection()

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
