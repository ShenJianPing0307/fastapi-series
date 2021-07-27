from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()

app.add_middleware(
    GZipMiddleware,
    minimum_size=1000
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*.example.com"]
)

app.add_middleware(HTTPSRedirectMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1",
        "http://127.0.0.1:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/items/")
async def get_items():
    items = [
        {"name": "apple", "price": "1.12"},
        {"name": "pear", "price": "3.14"}
    ]
    return items
