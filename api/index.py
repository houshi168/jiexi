from fastapi import FastAPI
import httpx

app = FastAPI()

# 使用一个稳定的第三方解析 API
API_ENDPOINT = "https://api.douyin.wtf/api?url="

@app.get("/api/index")
async def parse(url: str):
    try:
        async with httpx.AsyncClient() as client:
            # 直接转发链接给成熟的解析接口
            response = await client.get(API_ENDPOINT + url, timeout=15.0)
            
            # 关键修改：不要直接调用 response.json()，先检查内容
            content = response.text
            try:
                return response.json()
            except:
                return {"status": "failed", "error": "第三方API未返回JSON", "raw_content": content[:100]}
    except Exception as e:
        return {"status": "failed", "error": str(e)}
