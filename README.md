# DevOps-проект для портфолио

Простой DevOps-проект, демонстрирующий навыки контейнеризации, автоматизации, CI/CD и IaC. Использует Flask, Docker, Ansible, Terraform, MinIO и GitLab CI/CD, Prometheus + Grafana + Loki + Promtail, Trivy (сканирование образов), Semgrep (анализ кода) в CI


## Что делает проект

Приложение на Flask возвращает "Hello from DevOps!". Всё контейнеризовано и разворачивается через Ansible. Инфраструктура описана в Terraform. GitLab CI/CD автоматизирует сборку и деплой. Добавлен мониторинг с Prometheus и Grafana для отслеживания состояния приложения и инфраструктуры. Используется Trivy для автоматического сканирования Docker-образов и зависимостей на уязвимости перед деплоем.

## Технологии

- Python + Flask — веб-приложение
- Docker — контейнеризация
- Ansible — настройка серверов
- Terraform — инфраструктура как код
- GitLab CI/CD — автоматизация
- MinIO — локальное S3 (аналог Ceph)
- Prometheus + Grafana + Loki + Promtail
- Trivy (сканирование образов), Semgrep (анализ кода) в CI

## Запуск

1. Клонировать:  
   `git clone https://gitlab.com/username/devops-project.git`

2. Собрать и запустить контейнер:  
   `docker build -t flask-app ./app`  
   `docker run -d -p 5000:5000 flask-app`

3. Применить Ansible:  
   `ansible-playbook -i inventory site.yml`

4. Запустить Terraform:  
   `cd terraform && terraform init && terraform apply -auto-approve`

5. GitLab CI/CD:  
   Пайплайн запускается автоматически при push.
   
6. - Мониторинг: Prometheus + Grafana + Loki + Promtail через docker-compose
- DevSecOps: Trivy (сканирование образов), Semgrep (анализ кода) в CI

## Что показывает

- Владение Docker и Python
- Автоматизация развертывания
- CI/CD пайплайны
- Управление инфраструктурой через Terraform
