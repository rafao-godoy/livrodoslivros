import os
from fastapi import FastAPI
from database import criar_tabela
from pydantic import BaseModel
from database import salvar_ideia
from database import listar_ideias
from fastapi import Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse


templates = Jinja2Templates(directory="templates")

app = FastAPI(title="Livro dos Livros")

APP_PASSWORD = os.environ.get("APP_PASSWORD")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
def startup():
    criar_tabela()

class Ideia(BaseModel):
    titulo: str | None = None
    conteudo: str
    rotulos: str | None = None

@app.get("/", response_class=HTMLResponse)
def home(request: Request, password: str | None = None):
    if password != APP_PASSWORD:
        return HTMLResponse("""
            <h3>🔒 Área protegida</h3>
            <form method="get">
                <input type="password" name="password" placeholder="Senha">
                <button type="submit">Entrar</button>
            </form>
        """)

    ideias = listar_ideias()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "ideias": ideias}
    )


@app.post("/ideias/form")
def criar_ideia_form(
    titulo: str = Form(None),
    conteudo: str = Form(...),
    rotulos: str = Form(None)
):
    salvar_ideia(titulo, conteudo, rotulos)
    return {"status": "ok"}


@app.post("/ideias")
def criar_ideia(ideia: Ideia):
    salvar_ideia(ideia.titulo, ideia.conteudo, ideia.rotulos)
    return {"status": "salvo"}

@app.get("/ideias")
def obter_ideias():
    return listar_ideias()
