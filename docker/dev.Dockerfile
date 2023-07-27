FROM python:3.10

WORKDIR /workspace

RUN apt-get update && apt-get install -y jq zip curl python3-pip python3-venv && \
    curl -sL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

RUN pip install --upgrade pip && pip install cookiecutter

COPY aiverify/ /workspace/aiverify/
RUN cd aiverify/ai-verify-shared-library && npm install && npm run build && \
    pip install -r ../test-engine-core/requirements.txt

COPY ai-verify-plugin/ /workspace/ai-verify-plugin/
RUN cd ai-verify-plugin && npm install -g

CMD ["bash"]