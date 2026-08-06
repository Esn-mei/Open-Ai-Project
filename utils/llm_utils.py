# utils/llm_utils.py

from langchain_openai import ChatOpenAI
from config.lm_config import lm_config
import logging

logger = logging.getLogger(__name__)

try:
    # 初始化 ChatOpenAI 客户端
    chat_model = ChatOpenAI(
        model=lm_config.vl_model,
        api_key=lm_config.api_key,
        base_url=lm_config.base_url,
        temperature=lm_config.llm_temperature
    )

    # 可选：添加一个简单的测试调用，验证连接是否正常
    # test_response = chat_model.invoke([{"role": "user", "content": "test"}])
    # logger.info("LLM client initialized successfully")

except Exception as e:
    logger.error(f"LLM client initialization failed: {e}")
    chat_model = None


def get_vl_client():
    """获取视觉语言模型客户端实例（别名函数，提高可读性）"""
    return chat_model


_llm_client_cache = {}


def get_llm_client(model: str | None = None, json_mode: bool = False) -> ChatOpenAI:
    """
    获取 LangChain ChatOpenAI 客户端实例
    - model: 允许不同节点使用不同模型
    - json_mode: True 时要求输出 JSON
    """
    m = model or lm_config.llm_model
    key = (m, json_mode)
    if key in _llm_client_cache:
        return _llm_client_cache[key]

    extra_body = {"enable_thinking": False}

    model_kwargs: dict = {}
    if json_mode:
        model_kwargs["response_format"] = {"type": "json_object"}

    client = ChatOpenAI(
        model=m,
        temperature=lm_config.llm_temperature,
        api_key=lm_config.api_key,
        base_url=lm_config.base_url,
        extra_body=extra_body,
        model_kwargs=model_kwargs,
    )
    _llm_client_cache[key] = client
    return client

if __name__ == '__main__':
    # 测试代码
    client = get_llm_client()
    if client:
        try:
            response = client.invoke([{"role": "user", "content": "Hello"}])
            print(f"Test successful: {response.content}")
        except Exception as e:
            print(f"Test failed: {e}")
    else:
        print("LLM client is not available")