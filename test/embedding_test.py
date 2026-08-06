from utils.embedding_utils import  generate_embeddings

embeddings = generate_embeddings([
    "你好",
    "打印机如何安装驱动？",
    "设备支持哪些纸张尺寸？"
])
print(embeddings)