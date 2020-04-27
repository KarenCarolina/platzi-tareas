import sqlite3  

def listar_tareas():   
    try:
        
        conexion = sqlite3.connect("tareas.db")
    except:
          print("error") 
    else:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tabla_tareas;")
        tareas = cursor.fetchall()
    finally:
        conexion.close()  
    return tareas


def anadir_tareas(tarea):
    try:
        conexion = sqlite3.connect("tareas.db")
    except:
          print("error") 
    else:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO tabla_tareas  VALUES ( null ,'{}')".format(tarea))
        conexion.commit()
    finally:
        conexion.close()  


def editar_tareas(tarea, uid):
    try:
        conexion = sqlite3.connect("tareas.db")
    except:
          print("error") 
    else:
        cursor = conexion.cursor()
        cursor.execute("UPDATE tabla_tareas SET descripcion='{0}' WHERE id = '{1}' ;".format(tarea,uid))
        conexion.commit()
    finally:
        conexion.close()  


def borrar_tareas(uid):
    try: 
        conexion = sqlite3.connect("tareas.db")
    except:
          print("error") 
    else:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM tabla_tareas WHERE id='{}' ;".format(uid))
        conexion.commit()
    finally:
        conexion.close()  