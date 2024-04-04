# Stage 1
FROM node:alpine AS build
WORKDIR /app
COPY index.html .

# Stage 2
FROM nginx:alpine
COPY --from=build /app/index.html /usr/share/nginx/html/index.html
RUN mkdir -p /var/cache/nginx/client_temp \
    && chown -R nginx:nginx /var/cache/nginx \
    && chmod -R 755 /var/cache/nginx
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

