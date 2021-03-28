FROM node:lts-alpine
WORKDIR /app
COPY ./application .
RUN npm install
CMD ["npm", "run", "serve"]
