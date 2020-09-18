FROM 315948726009.dkr.ecr.sa-east-1.amazonaws.com/base/captalyspython:3.6
LABEL fileversion=v0.01

ARG RUN_ENVIRONMENT
ENV CURRENT_ENVIRONMENT=${RUN_ENVIRONMENT}
ENV DD_TRACE_ASGI_ANALYTICS=TRUE

# Para que os logs apareçam no datadog
ENV PYTHONUNBUFFERED=TRUE

WORKDIR /app/

COPY . .

RUN pip install -r requirements.txt --quiet

EXPOSE {{cookiecutter.api_port}}

ENTRYPOINT ["/bin/sh","/app/entrypoint.sh"]
