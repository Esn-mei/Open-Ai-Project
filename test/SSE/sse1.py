# test/sse/sse1.py

import asyncio
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

# 1. 初始化
app = FastAPI()

# 2. 跨域
app.add_middleware(
    CORSMiddleware,  # 启用跨域中间件
    allow_origins=["*"],  # 允许所有来源（任何网页都能调用）
    allow_credentials=True,  # 允许携带 Cookie
    allow_methods=["*"],  # 允许所有请求方式（GET/POST等）
    allow_headers=["*"],  # 允许所有请求头
)

# 3. 定义生成器函数
# 用 `async def` 定义，内部通过 `yield` 逐次返回数据（而非 `return` 一次性返回）；
# 每次 `yield` 都会向客户端推送一段数据，直到循环结束；
async def event_generator():
    # 模拟推5条消息，每秒1条
    for i in range(5):
        # ✅ 核心：SSE固定格式 data: 内容\n\n
        yield f"data: 这是第{i + 1}条测试消息\n\n"
        await asyncio.sleep(1)  # 每秒推1条
    # yield f"data: [END]\n\n"  # 结束标记

# 4. SSE接口
@app.get("/simple_stream")
async def simple_stream():
    # ✅ 核心：StreamingResponse + media_type=text/event-stream
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8001)