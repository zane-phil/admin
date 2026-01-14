# 1. 选基础镜像 (推荐 python 3.9 或 3.10)
FROM python:3.9-slim

RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list.d/debian.sources 2>/dev/null || sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list
RUN sed -i 's/security.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list.d/debian.sources 2>/dev/null || sed -i 's/security.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list

# 2. 设置工作目录
WORKDIR /app

# 3. 设置环境变量 (防止 Python 生成 .pyc 文件，保证日志直接输出)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 4. 安装系统依赖 (MySQL 客户端通常需要 gcc 等)
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# 5. 安装 Python 依赖
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt
# 生产环境必须装 Gunicorn
RUN pip install gunicorn

# 6. 复制项目代码
COPY . /app/

# 7. 赋予脚本执行权限 (可选)
# RUN chmod +x /app/docker_env/web/entrypoint.sh