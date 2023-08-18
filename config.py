# -*- coding:utf-8 -*-
"""
@Created on : 2023/8/18 12:20
@Author: mekesim
@Des: 基本配置文件
"""

import os
from dotenv import load_dotenv, find_dotenv
# from pydantic import BaseSettings
from pydantic_settings import BaseSettings
from typing import List


class Config(BaseSettings):
    # 加载环境变量
    load_dotenv(find_dotenv(), override=True)
    # 调试模式
    APP_DEBUG: bool = True
    # 项目信息
    VERSION: str = "0.0.1"
    PROJECT_NAME: str = "fasdapi"
    DESCRIPTION: str = '<a href="/redoc" target="_blank">redoc</a>'
    # 静态资源目录
    STATIC_DIR: str = os.path.join(os.getcwd(), "static")
    TEMPLATE_DIR: str = os.path.join(STATIC_DIR, "templates")
    # 跨域请求
    CORS_ORIGINS: List = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List = ["*"]
    CORS_ALLOW_HEADERS: List = ["*"]
    # Session
    SECRET_KEY:str = "session"
    SESSION_COOKIE:str = "session_id"
    SESSION_MAX_AGE: int = 14 * 24 * 60 * 60
    # Jwt
    JWT_SECRET_KEY:str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    JWT_ALGORITHM:str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 24 * 60

    SWAGGER_UI_OAUTH2_REDIRECT_URL:str = "/api/v1/test/oath2"

    # 二维码过期时间
    QRCODE_EXPIRE: int = 60 * 1


settings = Config()
