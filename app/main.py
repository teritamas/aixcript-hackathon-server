import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .utils.logging import logger


def get_application() -> FastAPI:
    logger.info("Start Setting")

    app = FastAPI(
        title="AI Cript Hackathon",
        description="AI Cript Hackathon APIです",
        prefix="/api/v1"
        # version=env_settings.version,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app: FastAPI = get_application()

if __name__ == "__main__":
    uvicorn.run(
        "__main__:app",
    )
