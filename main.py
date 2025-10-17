from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
from datetime import datetime, timezone

app = FastAPI()

CATFACT_URL = "https://catfact.ninja/fact"
FALLBACK_FACT = "Cats are mysterious creatures loved by many."

@app.get("/me")
def get_me():
    """Return profile info with a dynamic cat fact and current UTC timestamp."""
    # Try to fetch a cat fact (timeout so we don't hang)
    try:
        resp = requests.get(CATFACT_URL, timeout=5)
        resp.raise_for_status()
        fact = resp.json().get("fact", FALLBACK_FACT)
    except Exception:
        # If anything goes wrong, use a safe fallback fact
        fact = FALLBACK_FACT

    payload = {
        "status": "success",
        "user": {
            "email": "inuwahafsah@gmail.com",
            "name": "Hafsah Sanusi Inuwa",
            "stack": "Python/FastAPI"
        },
        # Current UTC time in ISO 8601 format
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": fact
    }
    return JSONResponse(content=payload, media_type="application/json")