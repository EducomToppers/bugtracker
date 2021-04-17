FROM node:15.13.0-alpine3.10
WORKDIR /app
COPY ./application/package.json .
COPY ./application/package-lock.json .
COPY ./application .
RUN npm install
RUN npm run build
CMD ["npm", "run", "serve"]
