import logging

# REIHENFOLGE beachten
# Konfiguration muss am Anfang kommen

sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
fh = logging.FileHandler('test.log')
fh.setLevel(logging.WARNING)

logging.basicConfig(level=logging.DEBUG, handlers=(sh, fh))

logging.warning('Hallo Welt')

logging.debug('Guten morgen')
logging.info('test')
