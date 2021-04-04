FROM node:15.13.0-alpine3.10
WORKDIR /app
COPY ./application .
RUN npm install
CMD ["npm", "run", "serve"]
