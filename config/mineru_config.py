from dataclasses import dataclass

from dotenv import load_dotenv
import os
load_dotenv()

@dataclass
class MineruConfig:
    base_url:str
    api_token:str

mineru_config=MineruConfig(
    base_url=os.getenv("MINERU_BASE_URL",""),
    api_token=os.getenv("MINERU_API_TOKEN","")
)

