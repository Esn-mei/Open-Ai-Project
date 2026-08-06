# utils/minio_utils.py

import json
from minio import Minio
from config.minio_config import minio_config
try:
    minio_client = Minio(
        endpoint=minio_config.endpoint,
        access_key=minio_config.access_key,
        secret_key=minio_config.secret_key,
        secure=False)
    # secure=False 是否启用HTTPS加密连接；False=用HTTP，True=用HTTPS；本地/内网部署一律写False
    if not minio_client.bucket_exists(minio_config.bucket_name):
        minio_client.make_bucket(minio_config.bucket_name)

    # exits=minio_client.bucket_exists("knowledge-base")
    # print(exits)


    # 设置存储桶策略为 Public Read (只读权限开放给匿名用户)
    # 这样前端可以直接通过 URL 访问图片，而不需要预签名 URL
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {"AWS": ["*"]},
                "Action": ["s3:GetObject"],
                "Resource": [f"arn:aws:s3:::{minio_config.bucket_name}/*"]
            }
        ]
    }
    minio_client.set_bucket_policy(minio_config.bucket_name, json.dumps(policy))
except Exception as e:
    print("Minio init failed:{e}")
    minio_client = None

def get_minio_client():
    return minio_client

if __name__ == '__main__':
    minio_client=get_minio_client()
    print(minio_client.bucket_exists("a123"))