from db.db import conn

cursor = conn.cursor()

def ToDo (data:dict):
    if not data ["title"] or not data ["description"] or not data ["date"]:
        return(False, "Titulo, descripcion y fecha son obligatorios")
    try:
        cursor.execute ("INSERT INTO activities (titulo, descripcion, fecha) VALUES (%s,%s,%s)", (data["title"],data["description"],data["date"]))
        conn.commit()
        return(True, "Actividad registrada con éxito")
    except Exception as e:
        print(e)
        return(False, "Ocurrió un error al guardar la actividad")