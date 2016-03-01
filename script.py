#!/home/miguel/.virtualenvs/redes/bin/python
import subprocess
import urllib2
import transmissionrpc
import time


host = "http://proyectoredes-gdoredes.rhcloud.com"
# host = "http://localhost:5000"
timestamp = time.strftime("[%d-%b-%Y:%X]")


def print_logs(log):
    archivo = open('script.log', 'a')
    archivo.write(log)
    archivo.close()


def reemplazar_caracteres_especiales(dato):
    dato = dato.replace(" ", "%20")
    dato = dato.replace("#", "%23")
    return dato


def cast_byte_to_human_readable(size):
    if(size / 1073741824) >= 1:
        size = str(round((float(size) / 1073741824), 2)) + " GB"
    elif(size / 1048576) >= 1:
        size = str(round((float(size) / 1048576), 2)) + " MB"
    elif (size / 1024) >= 1:
        size = str(round((float(size) / 1024), 2)) + " KB"
    else:
        size = str(size) + " B"
    return size


# Envia datos del Sistema Operativo
def datos_so():
    kernel = subprocess.check_output(['uname', '-s'])
    release = subprocess.check_output(['uname', '-r'])
    nodename = subprocess.check_output(['uname', '-n'])
    kernelv = subprocess.check_output(['uname', '-v'])
    machine = subprocess.check_output(['uname', '-m'])
    processor = subprocess.check_output(['uname', '-p'])
    os = subprocess.check_output(['uname', '-o'])
    hardware = subprocess.check_output(['uname', '-i'])
    string = kernel[:-1] + ',' \
                         + release[:-1] + ',' \
                         + nodename[:-1] + ',' \
                         + kernelv[:-1] + ',' \
                         + machine[:-1] + ',' \
                         + processor[:-1] + ',' \
                         + os[:-1] + ',' \
                         + hardware[:-1] + ',' \
                         + timestamp
    string = reemplazar_caracteres_especiales(string)

    # Envia datos del Sistema Operativo
    url = host + "/monitoreo/add/os/" + string
    try:
        req = urllib2.Request(url)
        res = urllib2.urlopen(req)
        message = timestamp + " " + res.read() + "\n"
    except urllib2.URLError:
        message = timestamp + " " + "Error al enviar los datos al servidor de OS\n"
    return message


# Envia datos de usurios activos
def datos_who():
    who = subprocess.Popen(['who'], stdout=subprocess.PIPE)
    cut = subprocess.Popen(['cut', '-d', ' ', '-f', '1'], stdin=who.stdout, stdout=subprocess.PIPE)
    output = subprocess.check_output('uniq', stdin=cut.stdout)

    string = output[:-1] + ',' + timestamp
    string = reemplazar_caracteres_especiales(string)

    url = host + "/monitoreo/add/who/" + string
    try:
        req = urllib2.Request(url)
        res = urllib2.urlopen(req)
        message = timestamp + " " + res.read() + "\n"
    except urllib2.URLError:
        message = timestamp + " " + "Error al enviar los datos al servidor de Usuario\n"
    return message


# Envia datos del uso de la CPU
def datos_cpu():
    string = ""
    for x in range(14, 19):
        vmstat = subprocess.Popen(['vmstat'], stdout=subprocess.PIPE)
        tail = subprocess.Popen(['tail', '-n', '+3'], stdin=vmstat.stdout, stdout=subprocess.PIPE)
        tr = subprocess.Popen(['tr', '-s', ' '], stdin=tail.stdout, stdout=subprocess.PIPE)
        out = subprocess.check_output(['cut', '-d', ' ', '-f', str(x)], stdin=tr.stdout)
        string += out[:-1] + ","
    string = string[:-1] + ',' + timestamp
    string = reemplazar_caracteres_especiales(string)

    url = host + "/monitoreo/add/cpu/" + string
    try:
        req = urllib2.Request(url)
        res = urllib2.urlopen(req)
        message = timestamp + " " + res.read() + "\n"
    except urllib2.URLError:
        message = timestamp + " " + "Error al enviar los datos al servido del CPU\r"
    return message


# Envia datos del uso de la memoria
def datos_mem():
    string = ""
    for x in range(4, 8):
        vmstat = subprocess.Popen(['vmstat'], stdout=subprocess.PIPE)
        tail = subprocess.Popen(['tail', '-n', '+3'], stdin=vmstat.stdout, stdout=subprocess.PIPE)
        tr = subprocess.Popen(['tr', '-s', ' '], stdin=tail.stdout, stdout=subprocess.PIPE)
        out = subprocess.check_output(['cut', '-d', ' ', '-f', str(x)], stdin=tr.stdout)
        string += cast_byte_to_human_readable(int(out[:-1] + '000')) + ","
    string = string[:-1] + ',' + timestamp
    string = reemplazar_caracteres_especiales(string)

    url = host + "/monitoreo/add/mem/" + string
    try:
        req = urllib2.Request(url)
        res = urllib2.urlopen(req)
        message = timestamp + " " + res.read() + "\n"
    except urllib2.URLError:
        message = timestamp + " " + "Error al enviar los datos al servidor de la Memoria\n"
    return message


# Envia datos del uso del swap
def datos_swap():
    string = ""
    for x in range(8, 10):
        vmstat = subprocess.Popen(['vmstat'], stdout=subprocess.PIPE)
        tail = subprocess.Popen(['tail', '-n', '+3'], stdin=vmstat.stdout, stdout=subprocess.PIPE)
        tr = subprocess.Popen(['tr', '-s', ' '], stdin=tail.stdout, stdout=subprocess.PIPE)
        out = subprocess.check_output(['cut', '-d', ' ', '-f', str(x)], stdin=tr.stdout)
        string += cast_byte_to_human_readable(int(out[:-1] + '000')) + ","
    string = string[:-1] + ',' + timestamp
    string = reemplazar_caracteres_especiales(string)

    url = host + "/monitoreo/add/swap/" + string
    try:
        req = urllib2.Request(url)
        res = urllib2.urlopen(req)
        message = timestamp + " " + res.read() + "\n"
    except urllib2.URLError:
        message = timestamp + " " + "Error al enviar los datos al servidor del Swap\n"
    return message


# Envia datos de las descarga por torrents
def datos_descargas():
    message = ""
    try:
        tc = transmissionrpc.Client('localhost', port=9091, user='miguel', password='123456')
        torrents = tc.get_torrents()
        for torrent in torrents:
            id = str(torrent.id)
            cod_hash = str(torrent.hashString)
            done = str(torrent.percentDone*100) + "%25"
            have = str(cast_byte_to_human_readable(torrent.downloadedEver))
            try:
                eta = str(torrent.eta)
            except:
                eta = "Unknown"
            up = str(torrent.rateUpload)
            down = str(torrent.rateDownload/1024)
            status = str(torrent.status)
            name = str(torrent.name)

            string = id + "," \
                        + cod_hash[:10] + "," \
                        + done + "," \
                        + have + "," \
                        + eta + "," \
                        + up + "," \
                        + down + "," \
                        + status + "," \
                        + name + "," \
                        + timestamp
            string = reemplazar_caracteres_especiales(string)
            url = host + "/transmission/add/torrent/" + string
            try:
                req = urllib2.Request(url)
                res = urllib2.urlopen(req)
                message += timestamp + " " + res.read() + "\n"
            except urllib2.URLError:
                message += timestamp + " " + "Error al enviar los datos al servidor del Status de torrents\n"
    except transmissionrpc.TransmissionError:
        message = timestamp + " " + "Error al conectarse con el transmission\n"
    return message


def captura_torrents():
    message = ""
    url = host + "/transmission/get/torrents/"
    try:
        req = urllib2.Request(url)
        res = urllib2.urlopen(req)
        a = res.read()
        print(res.read())
        array = a.split(",")

        for arr in array:
            ar = arr.split(";")
            if ar[0] and ar[1]:
                message += download_links(ar[0], ar[1])
    except urllib2.URLError:
        message = timestamp + " " + "Error al conectarse con el servidor para capturar torrents\n"
    return message


def download_links(id_torrent, magnet_link):
    message = timestamp + " " + "Exito Descargando el link " + magnet_link[:20] + "\n"
    try:
        tc = transmissionrpc.Client('localhost', port=9091, user='miguel', password='123456')
        tc.add_torrent(magnet_link)
        url = host + "/transmission/confirm/torrent/" + id_torrent
        try:
            req = urllib2.Request(url)
            res = urllib2.urlopen(req)
        except urllib2.URLError:
            message = timestamp + " " + "Error al conectarse con el servidor para enviar la verificacion de llegada\n"
    except transmissionrpc.TransmissionError:
        message = timestamp + " " + "Error descargando el link " + magnet_link[:20] + "\n"
    return message


# captura_torrents()
def enviar_datos():
    print_logs(datos_so())
    print_logs(datos_who())
    print_logs(datos_cpu())
    print_logs(datos_mem())
    print_logs(datos_swap())
    print_logs(datos_descargas())
    print_logs(captura_torrents())

enviar_datos()


