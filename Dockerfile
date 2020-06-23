FROM python:3.7-alpine
WORKDIR /app
COPY . .
RUN ln -s /app/terminal-math.py /usr/bin/m
CMD ["sh"]