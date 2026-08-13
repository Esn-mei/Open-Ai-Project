# test/fastapi/异步1.py
import asyncio

async def download_file(name):
    print(f"开始下载：{name}")
    await asyncio.sleep(2)  # 模拟下载耗时 2 秒（让出控制权2秒，非阻塞）
    print(f"下载完成：{name}")
async def main():
    # 三个任务同时开始！
    await asyncio.gather(
        download_file("文件 1"),
        download_file("文件 2"),
        download_file("文件 3")
    )

asyncio.run(main())