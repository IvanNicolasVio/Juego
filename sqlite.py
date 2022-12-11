import sqlite3

def crear_base_datos():
    with sqlite3.connect("db_btf.db") as conexion:
        try:
            sentencia = ''' create table pesronajes
                            (   
                                id integer primary key autoincrement,
                                nombre text,
                                score real,
                                nivel text,
                            )
                        '''
            conexion.execute(sentencia)
            print("Se creo la tabla personajes")
        except sqlite3.OperationalError:
            print("La tabla de personajes ya existe")

def actualizar_base_datos(name,player_1,nivel):
    with sqlite3.connect("db_btf.db") as conexion:
        try:
            conexion.execute("insert into personajes(nombre,score,nivel) values (?,?,?)",(name,player_1.score,nivel))
            conexion.commit()# actualiza los datos realmnente
        except:
            print("Error")