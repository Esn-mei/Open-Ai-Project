import base64

from langchain_openai import ChatOpenAI

from config.lm_config import lm_config

base_str = None
base_url=lm_config.base_url
api_key=lm_config.api_key
with open("D:\Agent\output\Agent开发实习简历\images\938231cebe8fb10e4a5a6f076203646b4ef190d64fe4d181c5ff31390a6ccd8a.jpg","rb") as img:
    base_str = base64.b64encode(img.read()).decode("utf-8")
print(base_url,api_key)
vl_ai = ChatOpenAI(model=lm_config.vl_model, temperature=lm_config.llm_temperature, base_url=lm_config.base_url,
        api_key=lm_config.api_key, model_kwargs={"response_format": {"type": "json_object"}})

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": f"""这是"11"文件中的一张图片，图片上文部分为"11"，下文部分为"11"，请用中文简要总结这张图片的内容，用于 Markdown 图片标题。"""
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base_str}"
                }
            }
        ]
    }
]
response = vl_ai.invoke(messages)
print(response)
# vl_ai = get_llm_client(lm_config.vl_model)