#!/bin/bash

# Переменная с образом
IMAGE_NAME="nginx:latest"  # Измените на нужный вам образ

# Проверка, установлен ли Docker
if ! command -v docker &> /dev/null; then
    echo "Docker не найден. Устанавливаем Docker..."

    # Установка Docker в зависимости от системы
    if [ -f /etc/debian_version ]; then
        sudo apt update
        sudo apt install -y docker.io
    elif [ -f /etc/redhat-release ]; then
        sudo yum install -y docker
    else
        echo "Неизвестная система. Установите Docker вручную."
        exit 1
    fi

    # Запуск и включение Docker
    sudo systemctl start docker
    sudo systemctl enable docker
fi

echo "Docker установлен и запущен."

# Проверка, загружен ли образ
if ! docker image inspect "$IMAGE_NAME" &> /dev/null; then
    echo "Образ $IMAGE_NAME не найден. Скачиваем..."
    docker pull "$IMAGE_NAME"
fi

# Запуск контейнера
echo "Запускаем контейнер с образом $IMAGE_NAME..."
docker run -d --name my_container -p 80:80 "$IMAGE_NAME"

echo "Контейнер успешно запущен!"

#!/bin/bash

JSON_FILE="foxycon-node-config.json"

cat > "$JSON_FILE" <<EOF
{
  "name": "example",
  "version": "1.0",
  "settings": {
    "enabled": true,
    "timeout": 30
  }
}
EOF

echo "Файл $JSON_FILE создан!"
