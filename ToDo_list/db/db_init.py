from db.db import conn

sql_schema ="""
CREATE TABLE IF NOT EXISTS activities(
    titulo VARCHAR(100) NOT NULL,
    descripcion TEXT NOT NULL,
    fecha date NOT NULL
);
"""

def iniciar_db():
    try:
        cursor = conn.cursor()
        cursor.execute(sql_schema)
        conn.commit()
        print("Tabla creada")
    except Exception as e:
        print(e)

iniciar_db()