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

# 4、接口接收session_id参数
@app.get("/stream/{session_id}")
async def stream_by_session(session_id: str):

    # 3. 定义生成器函数
    async def event_generator():
        for i in range(5):
            # 按session_id定制消息
            yield f"data: 会话{session_id} - 第{i + 1}条消息\n\n"
            await asyncio.sleep(1)
        yield f"data: [END]\n\n"  # 结束标记

    async def error_event_generator():
        # ⭐ 关键：不要 return，而是 yield 一个符合 SSE 格式的错误消息
        yield "data: 无效会话id\n\n"
        yield f"data: [END]\n\n"  # 结束标记

    if session_id == "123":
        return StreamingResponse(event_generator(), media_type="text/event-stream")
    else:
        return StreamingResponse(error_event_generator(), media_type="text/event-stream")



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8001)
