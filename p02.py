import logging

LOG_FORMAT = '%(asctime)s, %(levelname)s, %(message)s'

logging.basicConfig(level=logging.DEBUG, filename='p02.log', format=LOG_FORMAT)

logging.debug('this is a debug log')
logging.info('this is a  info log')
logging.warning('waring')
logging.error('error')
logging.critical('critical')


logging.log(logging.ERROR,'this is a error log')
logging.log(logging.CRITICAL,'this is a critical log')

