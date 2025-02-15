import logging

def setup_logger():
    logger = logging.getLogger("SalesforceTests")
    logger.setLevel(logging.INFO)  # You can change this to DEBUG for more detailed logs
    ch = logging.StreamHandler()  # This will print logs to the console
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(ch)

    return logger
