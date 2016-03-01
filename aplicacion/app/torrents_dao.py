import sys
from config import get_cursor, close_cursor
from time import strftime

def add_torrent_cola(nombre, magnet):
    cur = get_cursor()
    query = "INSERT INTO cola_torrents(nombre, magnet, magnet_short, state, fecha) VALUES (%s, %s, %s, %s, %s);"
    try:
        cur.execute(query, [nombre, magnet, magnet[:50], "PENDIENTE", strftime("[%d-%b-%Y:%X]")])
        conn = cur.connection
        conn.commit()
    except:
        return "Error al insertar la informacion de la cola de torrents " + str(sys.exc_info()[0])
    finally:
        close_cursor(cur)
    return "Exito al insertar la informacion de la cola de torrents"

def existe_torrent(hash):
    existe = False
    cur = get_cursor()
    query = "SELECT * FROM torrent WHERE hash = %s"
    try:
        cur.execute(query, [hash])
        array = cur.fetchall()
        if array:
            existe = True
    except:
        return "Error al retornar la informacion de existencia de torrents"

    finally:
        close_cursor(cur)

    return existe


def add_torrent_status(datos):
    array = datos.split(",")
    cur = get_cursor()
    if existe_torrent(array[1]):
        query = "UPDATE torrent SET cod_hash=%s," \
                "done=%s, " \
                "have=%s, " \
                "eta=%s, " \
                "up=%s, " \
                "down=%s, " \
                "status=%s, " \
                "name_torr=%s, " \
                "fecha=%s " \
                "WHERE id=%s"
    else:
        query = "INSERT INTO torrent(cod_hash, done, have, eta, up, down, status, name_torr, fecha, id) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    try:
        cur.execute(query, [array[1],
                            array[2],
                            array[3],
                            array[4],
                            array[5],
                            array[6],
                            array[7],
                            array[8],
                            array[9],
                            array[0]])
        conn = cur.connection
        conn.commit()
    except:
        return "Error al insertar la informacion del estado del torrent " + str(sys.exc_info()[0])
    finally:
        close_cursor(cur)

    return "Exito al insertar la informacion del estado del torrents con hash " + array[1][:5]


# Metodo encargado de retornar un resulset con la consulta de toda la cola de torrentes pendiente
def get_torrent_cola():
    cur = get_cursor()
    query = "SELECT * FROM cola_torrents ORDER BY id ;"
    try:
        cur.execute(query)
        arrays = cur.fetchall()
    except:
        return "Error al retornar la informacion de la cola de los torrents"

    finally:
        close_cursor(cur)
    return arrays

# Metodo encargado de retornar un resulset con la consulta de todas las descargas en el pc remoto
def get_torrent_status():
    cur = get_cursor()
    try:
        query = "SELECT * FROM torrent ORDER BY id ;"
        cur.execute(query)
        arrays = cur.fetchall()
    except:
        return "Error al retornar la informacion del estado de los torrents"

    finally:
        close_cursor(cur)
    return arrays

def change_torrente_state(id, state):
    cur = get_cursor()
    query = "UPDATE cola_torrents SET state=%s WHERE id=%s;"
    try:
        cur.execute(query, [state, id])
        conn = cur.connection
        conn.commit()
    except:
        return "Error al modificar el estado de los torrents"
    finally:
        close_cursor(cur)
    return "Exito al modificar el estado de los torrents"
