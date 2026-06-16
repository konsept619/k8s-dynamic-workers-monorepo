FROM python:3.12-slim

USER 0

WORKDIR /app

COPY src/ /app/

ENV PYTHONUNBUFFERED=1

USER 1001

CMD ["python", "main.py"]

