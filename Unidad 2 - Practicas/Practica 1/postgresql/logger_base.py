import logging as log

log.basicConfig(
    level=log.DEBUG,       #Nivel de debug, más bajo nivel es debug. debug, audit, warning, error, critical
    format="%(asctime)s : %(levelname)s [%(filename)s]:%(lineno)s %(message)s",
    datefmt='%I:%M:%S %p',
    handlers=[
        log.FileHandler('capa_datos.log'),
        log.StreamHandler()
    ]
)