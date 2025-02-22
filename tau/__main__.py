"""Main entry point for the tau package."""

import uvicorn

from tau import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
