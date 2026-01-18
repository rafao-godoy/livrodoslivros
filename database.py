import sqlite3

DB_NAME = "livro.db"

def get_connection():
    return sqlite3.connect(DB_NAME)


def criar_tabela():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ideias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            conteudo TEXT NOT NULL,
            rotulos TEXT,
            criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

def salvar_ideia(titulo, conteudo, rotulos):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO ideias (titulo, conteudo, rotulos)
        VALUES (?, ?, ?)
    """, (titulo, conteudo, rotulos))

    conn.commit()
    conn.close()

def listar_ideias():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, titulo, conteudo, rotulos, criado_em
        FROM ideias
        ORDER BY criado_em DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    ideias = []
    for row in rows:
        ideias.append({
            "id": row[0],
            "titulo": row[1],
            "conteudo": row[2],
            "rotulos": row[3],
            "criado_em": row[4]
        })

    return ideias
