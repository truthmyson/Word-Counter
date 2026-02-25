FROM nginx:alpine

# Copy static files and templates
COPY templates/ /templates
COPY scripts/ /scripts

# Copy custom Nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
