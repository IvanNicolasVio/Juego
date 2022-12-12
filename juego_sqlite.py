import sqlite3

def crear_base_datos():
    with sqlite3.connect("score.db") as conexion:
        try:
            sentencia = ''' CREATE TABLE jugadores
                            (   
                                    id integer primary key AUTOINCREMENT,
                                    nombre text,
                                    score real,
                                    nivel text
                            )
                        '''
            conexion.execute(sentencia)
            conexion.commit()# actualiza los datos realmnente
            print("Se creo la tabla jugadores")
        except sqlite3.OperationalError:
            print("La tabla de jugadores ya existe")

def actualizar_base_datos(name,player_1,nivel):
    with sqlite3.connect("score.db") as conexion:
        try:
            conexion.execute("INSERT INTO jugadores(nombre,score,nivel) values (?,?,?)",(name,player_1,nivel))
            conexion.commit()# actualiza los datos realmnente
        except:
            print("Error")

def eliminar_filas(id):
    with sqlite3.connect("score.db") as conexion:
            sentencia = "DELETE FROM jugadores WHERE id=?"
            conexion.execute(sentencia,(id,))


def ordenar_score():
    lista_score = []
    with sqlite3.connect("score.db") as conexion:
        sentencia = '''
                        SELECT nombre, score, nivel
                        FROM jugadores
                        ORDER BY score DESC
                        LIMIT 7        
                    '''
        cursor = conexion.execute(sentencia)
        for fila in cursor:
            lista_score.append(fila)

    return lista_score

