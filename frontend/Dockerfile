FROM node:18-alpine
WORKDIR /app
COPY ../../../project-docker-k8s%202/frontend/package.json ./
RUN npm install
COPY ../../../project-docker-k8s%202/frontend .
RUN npm run build
EXPOSE 3000
CMD ["npx", "serve", "-s", "build", "-l", "3000"]
