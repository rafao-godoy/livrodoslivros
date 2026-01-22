📘 Livro dos Livros

Aplicação pessoal para captura, organização e consulta de ideias, desenvolvida em Python com FastAPI, com interface web transformada em PWA (Progressive Web App) e deploy em nuvem.
O objetivo do projeto é unir produtividade pessoal com boas práticas de desenvolvimento, servindo também como exemplo de portfólio para freelancing.

---------------------------------------------------------------------------------------------------------------------------------------------------

✨ Funcionalidades

✍️ Criar ideias (título, conteúdo e rótulos)
📋 Listar ideias em ordem cronológica
📱 Aplicativo instalável (PWA)
☁️ Rodando na nuvem (Render)
🗄️ Banco de dados persistente (PostgreSQL)
🔐 Proteção por senha simples (MVP)

---------------------------------------------------------------------------------------------------------------------------------------------------

🛠️ Tecnologias utilizadas

Python 3.13
FastAPI
Uvicorn
PostgreSQL
psycopg2
Jinja2
HTML
PWA (Manifest + Service Worker)
Render (Deploy em nuvem)

---------------------------------------------------------------------------------------------------------------------------------------------------

🧱 Arquitetura (resumo)

Backend em FastAPI
Templates HTML renderizados no servidor
Banco de dados PostgreSQL gerenciado pelo Render
Variáveis sensíveis via Environment Variables
Deploy automático via GitHub + Render

---------------------------------------------------------------------------------------------------------------------------------------------------

🚀 Como rodar localmente

git clone https://github.com/seu-usuario/livro-dos-livros.git
cd livro-dos-livros

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
uvicorn main:app --reload

Acesse:
http://127.0.0.1:8000

---------------------------------------------------------------------------------------------------------------------------------------------------

🔐 Variáveis de ambiente
Variável	Descrição
DATABASE_URL	URL de conexão com PostgreSQL
APP_PASSWORD	Senha simples de acesso ao app

---------------------------------------------------------------------------------------------------------------------------------------------------

📱 PWA

O app pode ser instalado no celular diretamente pelo navegador:

Android: Adicionar à tela inicial

iOS: Compartilhar → Adicionar à Tela de Início

O aplicativo funciona em tela cheia, como um app nativo.

---------------------------------------------------------------------------------------------------------------------------------------------------

🎯 Próximos passos (roadmap)

✏️ Editar ideias
🗑️ Excluir ideias
💬 Integração com WhatsApp (Twilio)
🔍 Busca por termos
👤 Autenticação por usuário

---------------------------------------------------------------------------------------------------------------------------------------------------

👨‍💻 Autor

Projeto desenvolvido por Rafael Godoy, como aplicação pessoal e estudo prático de backend, deploy em nuvem e integração futura com APIs externas.


