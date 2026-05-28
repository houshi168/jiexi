from fastapi import FastAPI
import httpx

app = FastAPI()

# 稳定的第三方解析 API
API_ENDPOINT = "https://api.douyin.wtf/api?url="

@app.get("/api/index")
async def parse(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(API_ENDPOINT + url, timeout=15.0)
        return response.json()
