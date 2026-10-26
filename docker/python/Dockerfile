FROM python:3.13.17-slim-trixie

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y git

COPY ./app/requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

RUN addgroup --system app && adduser --system --group app
USER app

CMD ["python", "main.py"]
