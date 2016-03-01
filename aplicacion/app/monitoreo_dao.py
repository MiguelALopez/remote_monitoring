import sys
from config import get_cursor, close_cursor

def add_data_os(datos):
    array = datos.split(",")
    cur = get_cursor()
    try:
        query = "INSERT INTO os(kernel, release, nodename, kernelversion, machine, processor, operatingsystem, hardware, fecha)" \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        cur.execute(query, [array[0],
                            array[1],
                            array[2],
                            array[3],
                            array[4],
                            array[5],
                            array[6],
                            array[7],
                            array[8]])
        conn = cur.connection
        conn.commit()
    except:
        return "Error al insertar la informacion del OS " + str(sys.exc_info()[0])
    finally:
        close_cursor(cur)

    return "Exito al insertar la informacion del OS"


def add_data_who(datos):
    array = datos.split(",")
    cur = get_cursor()
    try:
        query = "INSERT INTO who(nombre, fecha) VALUES (%s, %s);"
        cur.execute(query, [array[0],
                            array[1]])
        conn = cur.connection
        conn.commit()
    except:
        return "Error al insertar la informacion de los Usuarios " + str(sys.exc_info()[0])
    finally:
        close_cursor(cur)

    return "Exito al insertar la informacion de los Usuarios"


def add_data_cpu(datos):
    array = datos.split(",")
    cur = get_cursor()
    try:
        query = "INSERT INTO cpu(usuario, sistema, idle, waiting, stolen, fecha) VALUES (%s, %s, %s, %s, %s, %s);"
        cur.execute(query, [array[0],
                            array[1],
                            array[2],
                            array[3],
                            array[4],
                            array[5]])
        conn = cur.connection
        conn.commit()
    except:
        return "Error al insertar la informacion de la CPU " + str(sys.exc_info()[0])
    finally:
        close_cursor(cur)

    return "Exito al insertar la informacion de la CPU"


def add_data_mem(datos):
    array = datos.split(",")
    cur = get_cursor()
    try:
        query = "INSERT INTO mem(swpd, free, buff, cache, fecha) VALUES (%s, %s, %s, %s, %s);"
        cur.execute(query, [array[0],
                            array[1],
                            array[2],
                            array[3],
                            array[4]])
        conn = cur.connection
        conn.commit()

    except:
        return "Error al insertar la informacion de la Memoria " + str(sys.exc_info()[0])
    finally:
        close_cursor(cur)

    return "Exito al insertar la informacion de la Memoria"


def add_data_swap(datos):
    array = datos.split(",")
    cur = get_cursor()
    try:
        query = "INSERT INTO swap(si, so, fecha) VALUES (%s, %s, %s);"
        cur.execute(query, [array[0],
                            array[1],
                            array[2]])
        conn = cur.connection
        conn.commit()

    except:
        return "Error al insertar la informacion del Swap" + str(sys.exc_info()[0])
    finally:
        close_cursor(cur)

    return "Exito al insertar la informacion del Swap"

def get_data_os():
    cur = get_cursor()
    try:
        query = "SELECT * FROM os ORDER BY id"
        cur.execute(query)
        arrays = cur.fetchall()

    except:
        return "Error al retornar la informacion del OS"

    finally:
        close_cursor(cur)

    return arrays


def get_data_who():
    cur = get_cursor()
    try:
        query = "SELECT * FROM who ORDER BY id"
        cur.execute(query)
        arrays = cur.fetchall()

    except:
        return "Error al retornar la informacion del Usuario"

    finally:
        close_cursor(cur)

    return arrays


def get_data_cpu():
    cur = get_cursor()
    try:
        query = "SELECT * FROM cpu ORDER BY id"
        cur.execute(query)
        arrays = cur.fetchall()

    except:
        return "Error al retornar la informacion de la CPU"

    finally:
        close_cursor(cur)

    return arrays


def get_data_mem():
    cur = get_cursor()
    try:
        query = "SELECT * FROM mem ORDER BY id"
        cur.execute(query)
        arrays = cur.fetchall()

    except:
        return "Error al retornar la informacion de la Memoria"

    finally:
        close_cursor(cur)

    return arrays


def get_data_swap():
    cur = get_cursor()
    try:
        query = "SELECT * FROM swap ORDER BY id"
        cur.execute(query)
        arrays = cur.fetchall()

    except:
        return "Error al retornar la informacion del Swap"

    finally:
        close_cursor(cur)

    return arrays