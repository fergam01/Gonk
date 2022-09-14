BOT_TOKEN: str = "OTg3NDU2OTg4MzMyMDY0ODY4.G3U3-m.v-Rnhv939ncFEWjjeN8uSTNKpe_MQTBlMFe0oQ"
SPOTIFY_ID: str = "1310faf218d54033829ebe6364f4a5af"
SPOTIFY_SECRET: str = "489c6235369b4a06b7a5dbf6eea4dab6"

BOT_PREFIX = "."

EMBED_COLOR = 0x4dd4d0  #replace after'0x' with desired hex code ex. '#ff0188' >> '0xff0188'

SUPPORTED_EXTENSIONS = ('.webm', '.mp4', '.mp3', '.avi', '.wav', '.m4v', '.ogg', '.mov')

MAX_SONG_PRELOAD = 5  #maximum of 25

COOKIE_PATH = "/config/cookies/cookies.txt"

GLOBAL_DISABLE_AUTOJOIN_VC = False

VC_TIMEOUT = 600 #seconds
VC_TIMOUT_DEFAULT = True  #default template setting for VC timeout true= yes, timeout false= no timeout
ALLOW_VC_TIMEOUT_EDIT = True  #allow or disallow editing the vc_timeout guild setting


STARTUP_MESSAGE = "Starting Bot..."
STARTUP_COMPLETE_MESSAGE = "Startup Complete"

NO_GUILD_MESSAGE = 'Error: Please join a voice channel or enter the command in guild chat'
USER_NOT_IN_VC_MESSAGE = "Error: Please join the active voice channel to use commands"
WRONG_CHANNEL_MESSAGE = "Error: Por favor usa el canal de comandos de musica"
NOT_CONNECTED_MESSAGE = "Error: el bot no esta conectado a ningun canal de voz"
ALREADY_CONNECTED_MESSAGE = "Error: El bot ya esta conectado en un canal de voz"
CHANNEL_NOT_FOUND_MESSAGE = "Error: No se encontro el canal indicado"
DEFAULT_CHANNEL_JOIN_FAILED = "Error: Could not join the default voice channel"
INVALID_INVITE_MESSAGE = "Error: Link de invitacion invalido"

ADD_MESSAGE= "Para añadir al bot a tu server, clickea [aca]" #brackets will be the link text

INFO_HISTORY_TITLE = "Songs Played:"
MAX_HISTORY_LENGTH = 10
MAX_TRACKNAME_HISTORY_LENGTH = 15

SONGINFO_UPLOADER = "Publicada por: "
SONGINFO_DURATION = "Duracion: "
SONGINFO_SECONDS = "s"
SONGINFO_LIKES = "Likes: "
SONGINFO_DISLIKES = "Dislikes: "
SONGINFO_NOW_PLAYING = "Tocando"
SONGINFO_QUEUE_ADDED = "Añadida a la cola"
SONGINFO_SONGINFO = "Info de la cancion"
SONGINFO_ERROR = "Error: Unsupported site or age restricted content. To enable age restricted content check the documentation/wiki."
SONGINFO_PLAYLIST_QUEUED = "Queued playlist :page_with_curl:"
SONGINFO_UNKNOWN_DURATION = "Unknown"

HELP_ADDBOT_SHORT = "Añade el bot a otro server"
HELP_ADDBOT_LONG = "Te da el link para agregar a Gonk a otro server tuyo."
HELP_CONNECT_SHORT = "Conecta a Gonk al canal de voz"
HELP_CONNECT_LONG = "Conecta a Gonk al canal de voz en el que estas actualmente"
HELP_DISCONNECT_SHORT = "Desconecta a Gonk"
HELP_DISCONNECT_LONG = "Desconecta a Gonk del canal de voz y para la musica."

HELP_SETTINGS_SHORT = "Te permite ver y modificar algunas config del bot"
HELP_SETTINGS_LONG = "Te permite ver y modificar algunas configuraciones del bot en el server. Uso: {}settings nombre_de_setting valor".format(BOT_PREFIX)

HELP_HISTORY_SHORT = "Muestra el historial de canciones"
HELP_HISTORY_LONG = "Muestra las " + str(MAX_TRACKNAME_HISTORY_LENGTH) + " ultimas canciones tocadas."
HELP_PAUSE_SHORT = "Pausa la musica"
HELP_PAUSE_LONG = "Pausa el reproductor de audio actual. Puede ser reanudado con el comando resume."
HELP_VOL_SHORT = "Cambia el volumen"
HELP_VOL_LONG = "Cambia el volumen del reproductor de audio. El argumento especifica el % de volumen que va a ser setteado."
HELP_PREV_SHORT = "Vuelve a tocar la cancion anterior"
HELP_PREV_LONG = "Toca la anterior cancion denuevo."
HELP_RESUME_SHORT = "Resume la musica"
HELP_RESUME_LONG = "Resume al Reproductor de  audio."
HELP_SKIP_SHORT = "Skippea la cancion"
HELP_SKIP_LONG = "Skippea la cancion actual y agarra la siguiente de la cola."
HELP_SONGINFO_SHORT = "Info de la cancion actual"
HELP_SONGINFO_LONG = "Muestra algunos detalles de la cancion que esta tocando actualmente, junto con el link de la misma."
HELP_STOP_SHORT = "Para la musica"
HELP_STOP_LONG = "Para el Reproductor de musica y borra la cola de canciones"
HELP_MOVE_LONG = f"{BOT_PREFIX}move [posicion a cambiar] [nueva posicion]"
HELP_MOVE_SHORT = 'Mueve determinada cancion en la lista'
HELP_YT_SHORT = "Reproduce el link indicado o la busca en Youtube"
HELP_YT_LONG = ("$p [link/video title/key words/playlist-link/soundcloud link/spotify link/bandcamp link/twitter link]")
HELP_PING_SHORT = "Pong"
HELP_PING_LONG = "El mejor comando del mundo (sirve para testear el nivel de respuesta del bot)"
HELP_CLEAR_SHORT = "Vacia la cola de canciones."
HELP_CLEAR_LONG = "Vacia la lista de canciones y skippea la cancion actual."
HELP_LOOP_SHORT = "Loopea la cancion que esta siendo reproduicida, funciona como on/off."
HELP_LOOP_LONG = "Hace un loop de la cacion actual y bloquea la cola de canciones reproduciendo siempre la misma. Usa este comando denuevo para romper el loop."
HELP_QUEUE_SHORT = "Muestra las canciones en cola."
HELP_QUEUE_LONG = "Muestra las canciones en cola (hasta 10)."
HELP_SHUFFLE_SHORT = "Mezcla las canciones en cola"
HELP_SHUFFLE_LONG = "Mezcla de manera random las canciones agregadas en cola"
HELP_CHANGECHANNEL_SHORT = "Cambia el canal en el que esta el bot"
HELP_CHANGECHANNEL_LONG = "Cambia el canal en el que esta el bot al que estas voz ahora mismo."

ABSOLUTE_PATH = '' #do not modify