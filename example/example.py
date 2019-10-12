import ezlogs

logger = ezlogs.Logger(file_name='log.txt', console_level='debug', file_level='debug')

logger.info('This is an informational message')
logger.debug('This is a debugging message')
