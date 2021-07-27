import logging
#import logging.config

logging.config.fileConfig(fname='master2.log',encoding='utf-8',level=logging.DEBUG,format='%(asctime)s %(message)s')

logger=logging.getLogger(__name__)
logger.debug(" This is warning msg")
logger.info("This is info msg")
logger.info("And this is warning msg")
logger.info("And non-ASCII stuff,too,like this")
logger.info("Hey this is SQA Tools")