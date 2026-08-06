import os
from langchain_openai import ChatOpenAI

# 1. 从你的配置中复制过来进行测试（测试完记得删掉这段代码里的 Key）
api_key = "sk-139eb92a25ff4604974d18c1cc9f0b71"  # 临时使用，测试完立即更换
base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
model_name = "qwen3-vl-flash"  # 请确认控制台里的准确名称

try:
    # 2. 初始化客户端
    llm = ChatOpenAI(
        api_key=api_key,
        base_url=base_url,
        model=model_name,
        temperature=0.1
    )

    # 3. 发送一个最简单的纯文本请求测试连通性
    response = llm.invoke([{"role": "user", "content": "你好，请回复 1"}])

    print("✅ 测试成功！返回结果：")
    print(response.content)

except Exception as e:
    print("❌ 测试失败，错误信息：")
    print(e)