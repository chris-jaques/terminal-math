FROM python:3.7-alpine
WORKDIR /app
COPY . .
ENTRYPOINT ["/app/terminal-math.py"]