from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI()
    @app.get("/health/")
    async def root():
        return {"status": "OK"}

    return app
