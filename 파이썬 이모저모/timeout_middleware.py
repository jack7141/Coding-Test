from fastapi import FastAPI, Request, HTTPException
from async_timeout import timeout
import time
import asyncio
import logging

_log = logging.getLogger(__file__)

app = FastAPI()


class TimeoutMiddleware:
    def __init__(self, app: FastAPI, timeout_seconds: int = 3):
        self.app = app
        self.timeout_seconds = timeout_seconds

    async def __call__(self, request: Request, call_next):
        start_time = time.time()
        try:
            async with timeout(self.timeout_seconds):
                response = await call_next(request)
            return response
        except asyncio.TimeoutError:
            _log.warning(
                f"TimeoutMiddleware: Request timed out after {time.time() - start_time} seconds.",
                extra={"path": request.url.path},
            )
            raise HTTPException(status_code=408, detail="Request timeout")


app.middleware("http")(TimeoutMiddleware(app, 5))


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/async-endpoint")
async def async_endpoint():
    await asyncio.sleep(3)  # Simulating a long async operation
    return {"Hello": "async"}


@app.get("/sync-endpoint")
def sync_endpoint():
    time.sleep(4)  # Simulating a long sync operation
    return {"Hello": "sync"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9999)
