FROM python:3.11-slim

WORKDIR /app

COPY dist/*.whl .


RUN pip install *.whl

ENTRYPOINT ["python", "-m", "example_fastapi_app", "--server-ip", "0.0.0.0"]

EXPOSE 8080