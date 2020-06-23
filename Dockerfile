FROM python:3.7
WORKDIR /app
COPY . .
ENV PATH="/app:${PATH}"
CMD ["sh"]