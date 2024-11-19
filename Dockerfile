FROM python:3.11-slim

RUN apt-get update && apt-get install -y git openssh-client && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /root/.ssh

COPY id_rsa /root/.ssh/id_rsa

RUN chmod 600 /root/.ssh/id_rsa

RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

COPY foxycon-node /app/foxycon-node

COPY requirements.txt /app/foxycon-node

RUN pip install --no-cache-dir -r /app/foxycon-node/requirements.txt

WORKDIR /app/foxycon-node

RUN rm -rf /root/.ssh

CMD ["alembic upgrade head; python start_node.py"]