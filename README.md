# 📅 Agenda App - Full Stack Django 6.0 Web Application Project

Esta é uma aplicação completa de agenda de conntatos, desenvolvida para gerenciar estes contatos, com foco em segurança, escalabilidade e deploy real em ambiente de nuvem da Google Cloud Platform.

## 🛠️ Tecnologias e Arquitetura
- **Django 6.0.5**: Framework principal.
- **Python 3.14.4**: Última versão disponível no momento do desenvolvimento.
- **Nginx & Gunicorn**: Stack de produção para servir a aplicação.
- **Google Cloud Platform**: Hospedagem da VM.
- **Segurança**: Uso de `ALLOWED_HOSTS` e separação de `local_settings.py` para proteção de credenciais.

## ⚙️ Diferenciais deste Projeto
- **Deploy em Produção**: Configuração completa de servidor Linux Ubuntu 26.04.
- **Arquitetura MVC**: Separação clara de responsabilidades.
- **Ambiente Isolado**: Configuração via `venv` e gerenciamento de dependências.

## 🔧 Como rodar o projeto localmente
1. Clone o repositório: `git clone ...`
2. Crie um venv: `python -m venv venv`
3. Ative o venv: `source venv/bin/activate` (Linux) ou `venv\Scripts\activate` (Windows)
4. Instale as dependências: `pip install -r requirements.txt`
5. Execute as migrações: `python manage.py migrate`
6. Rode o servidor: `python manage.py runserver`

## 👨‍💻 Autor
**Guilherme Nunes**
- [LinkedIn]((https://www.linkedin.com/in/guilherme-nunes-cea-575596203/))
