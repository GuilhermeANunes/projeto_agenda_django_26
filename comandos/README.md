Iniciar o projeto Django

python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
django-admin startproject project .
Configurar o git

git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT

# Para conectar o GitBash com o GitHub

eval $(ssh-agent)
ssh-add ~/.ssh/SEU_USUARIO