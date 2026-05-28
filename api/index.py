from fastapi import FastAPI
import httpx
import uvicorn

app = FastAPI()

API_ENDPOINT = "https://api.douyin.wtf/api?url="

@app.get("/")
async def parse(url: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(API_ENDPOINT + url, timeout=10.0)
            return response.json()
    except Exception as e:
        return {"status": "failed", "error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
