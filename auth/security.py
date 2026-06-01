import os
from fastapi import Header, HTTPException

API_KEY = os.getenv("HYBRID_API_KEY")


def verify_api_key(x_api_key: str = Header(None)):

    if not x_api_key:
        raise HTTPException(
            status_code=401,
            detail="API key missing"
        )

    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )