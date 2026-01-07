from fastapi import FastAPI

app = FastAPI(title="Livro dos Livros")

@app.get("/")
def home():
    return {"status": "ok", "mensagem": "Livro dos Livros rodando 📘"}
