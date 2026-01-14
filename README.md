# DvlyAdmin Mini Project

这是一个基于 **Django** 和 **Vue** 的前后端分离管理系统，采用 Docker 容器化部署。

## 🛠 技术栈 (Tech Stack)

本项目采用以下核心技术构建：

### 前端 (Frontend)
- **框架**: Vue.js (通过 Nginx 容器部署)
- **服务器**: Nginx (反向代理与静态资源服务)

### 后端 (Backend)
- **框架**: Django (Python)
- **应用服务器**: Gunicorn
- **WSGI 入口**: `application.wsgi`

### 数据存储与缓存 (Data & Cache)
- **数据库**: MySQL 8.0
- **缓存**: Redis (Alpine)

## 📂 服务架构

基于 `docker-compose.yml` 的服务编排：

| 服务名称 | 容器名 | 端口映射 | 说明 |
| :--- | :--- | :--- | :--- |
| **frontend** | `zane_frontend` | `80:80` | Nginx 前端入口，反向代理 API 请求 |
| **backend** | `zane_backend` | - | Django 后端 API 服务 (Gunicorn) |
| **db** | `zane_db` | `3306:3306` | MySQL 数据库 |
| **redis** | `zane_redis` | - | Redis 缓存服务 |

## 🚀 快速开始 (Getting Started)

本项目支持 Docker 一键启动，无需本地安装 Python 或 Node.js 环境。

### 1. 环境准备
- Docker
- Docker Compose

### 2. 启动服务

在项目根目录下运行以下命令：

```bash
# 构建并启动所有服务
docker-compose up -d --build
```

### 3. 访问项目

- **前端页面**: http://localhost
- **数据库连接**:
    - 主机: `localhost`
    - 端口: `3306`
    - 用户名: `root`
    - 密码: `123456` (开发环境默认)
    - 数据库名: `dvlyadmin_mini`

## ⚙️ 常用维护命令

### 查看日志
```bash
# 查看后端日志
docker logs -f zane_backend

# 查看数据库日志
docker logs -f zane_db
```

### 数据库初始化
项目启动时会自动加载 `./backend/dvlyadmin-mini.sql` 初始化数据库（仅限首次启动）。
如果需要手动重置数据库：

```bash
# 停止服务并删除卷数据
docker-compose down -v
# 重新启动
docker-compose up -d
```

### 进入容器
```bash
# 进入后端容器执行 Django 命令
docker exec -it zane_backend /bin/bash

# 示例：手动迁移数据库
# python manage.py migrate
```

## 📂 目录说明

- `backend/`: Django 后端源码及 Dockerfile
- `frontend/`: Vue 前端源码及 Dockerfile
- `docker-compose.yml`: 容器编排配置
- `dvlyadmin-mini.sql`: 数据库初始化脚本

## 📄 许可证 (License)

本项目遵循 MIT License 许可证。