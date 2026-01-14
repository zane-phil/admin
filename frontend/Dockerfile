# 第一阶段：构建 (Builder)
FROM node:18-alpine as builder

WORKDIR /app
# 复制 package.json 安装依赖
COPY package.json package-lock.json ./
# 这里的 npm install 如果卡顿，可以换淘宝源
RUN npm install --registry=https://registry.npmmirror.com

# 复制源代码并打包
COPY . .
RUN npm run build

# 第二阶段：运行 (Runner)
FROM nginx:alpine

# 1. 把第一阶段打包好的 dist 文件夹复制到 Nginx 目录
COPY --from=builder /app/dist /usr/share/nginx/html

# 2. 复制我们自定义的 Nginx 配置覆盖默认配置
COPY nginx.conf /etc/nginx/conf.d/default.conf

# 3. 暴露端口
EXPOSE 80