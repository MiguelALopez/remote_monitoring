from app import app
from app import monitoreo_dao, torrents_dao
from flask import render_template
from forms import MagnetLink


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/monitoreo.html')
def monitoreo():
    datos_os = monitoreo_dao.get_data_os()
    datos_who = monitoreo_dao.get_data_who()
    datos_cpu = monitoreo_dao.get_data_cpu()
    datos_mem = monitoreo_dao.get_data_mem()
    datos_swap = monitoreo_dao.get_data_swap()
    return render_template('monitoreo.html',
                           datos_os=datos_os,
                           datos_who=datos_who,
                           datos_cpu=datos_cpu,
                           datos_mem=datos_mem,
                           datos_swap=datos_swap)


@app.route('/transmission.html', methods=['GET', 'POST'])
def transmission():
    datos_torrents = torrents_dao.get_torrent_status()
    datos_torrents_cola = torrents_dao.get_torrent_cola()
    form = MagnetLink()
    if form.validate_on_submit():
        torrents_dao.add_torrent_cola(form.name_link.data, form.magnet_link.data, )
    return render_template('transmission.html',
                           datos_torrents=datos_torrents,
                           datos_torrents_cola=datos_torrents_cola,
                           form=form)


@app.route('/prueba/<prueba>')
def prueba(prueba):
    return prueba

# Usado para guardar los datos de el sistema operativo
@app.route("/monitoreo/add/os/<path:datos>")
def add_data_os(datos):
    return monitoreo_dao.add_data_os(datos)

# Usado para guardar los datos de el usuario conectado
@app.route("/monitoreo/add/who/<path:datos>")
def add_data_who(datos):
    return monitoreo_dao.add_data_who(datos)

# Usado para guardar los datos de la CPU
@app.route("/monitoreo/add/cpu/<path:datos>")
def add_data_cpu(datos):
    return monitoreo_dao.add_data_cpu(datos)

# Usado para guardar los datos de la memoria
@app.route("/monitoreo/add/mem/<path:datos>")
def add_data_mem(datos):
    return monitoreo_dao.add_data_mem(datos)

# Usado para guardar los datos del swap
@app.route("/monitoreo/add/swap/<path:datos>")
def add_data_swap(datos):
    return monitoreo_dao.add_data_swap(datos)

# Usado para retornar los magnet links para ser descargados en el pc remoto
@app.route("/transmission/get/torrents/")
def get_data_torrents_cola():
    array = torrents_dao.get_torrent_cola()
    string = ""
    for x in array:
        if x[4] != "CONFIRMADO":
            string += str(x[0]) + ";" + x[2] + ","
            torrents_dao.change_torrente_state(x[0], "ESPERA_CONFIRMACION")
    return string[:-1]


@app.route("/transmission/confirm/torrent/<path:torrent>")
def confirm_torrent(torrent):
    return torrents_dao.change_torrente_state(torrent, "CONFIRMADO")

# Usado para guardar la informacion del estado de los torrents que se estan en el pc remoto
@app.route("/transmission/add/torrent/<path:datos>")
def add_link(datos):
    return torrents_dao.add_torrent_status(datos)


app.WTF_CSRF_ENABLED = True
app.secret_key = 'you-will-never-guess'
