import logging
from Data_Driven_Framework_dummy_ticket.data.session_data import log_file_path
from Data_Driven_Framework_dummy_ticket.data.session_data import *
from Data_Driven_Framework_dummy_ticket.utilities.get_logger import custom_logger



def custom_logger():
    global logger

    #logger=logging.getLogger('test')
    logger=logging.getLogger(__name__)

    logger.setLevel(logging.DEBUG)
    #log_file=log_file_path
    log_file= 'debug.log'
    file_handler=logging.FileHandler(log_file,mode="a")
    file_handler.setLevel(logging.DEBUG)
    formatter=logging.Formatter("%(asctime)s - %(name)s -%(levelname)s:%(message)",datefmt='%m/%d/%Y   %I:%M:%S:%P')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(file_handler)
    return logger

log=custom_logger()
#log.info("Hello this is info logger")
log.info("This is warning")
