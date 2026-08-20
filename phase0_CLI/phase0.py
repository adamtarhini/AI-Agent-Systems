import asyncio
import os
import httpx
from dotenv import load_dotenv
from pydantic import BaseModel


class Settings(BaseModel):
    api_base_url: str
    timeout_seconds: float


load_dotenv()
settings = Settings(
    api_base_url=os.environ["API_BASE_URL"],
    timeout_seconds=float(os.environ.get("TIMEOUT_SECONDS", 5)),
)

paths = ["/todos/1", "/todos/2", "/todos/3"]


class Result(BaseModel):
    path: str
    status_code: int
    ok: bool


async def fetch(client, path):
    response = await client.get(path)
    return Result(path=path, status_code=response.status_code, ok=response.is_success)


async def main():
    async with httpx.AsyncClient(base_url=settings.api_base_url, timeout=settings.timeout_seconds) as client:
        results = await asyncio.gather(*[fetch(client, p) for p in paths])

    for r in results:
        print(r.path, "->", r.status_code, "OK" if r.ok else "FAILED")


asyncio.run(main())