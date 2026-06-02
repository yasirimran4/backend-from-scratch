# Logging module in Python provides a flexible framework for emitting log messages from Python programs.
#  It allows you to track events that happen when some software runs, which can be helpful 
# for debugging and monitoring the behavior of your application.

import logging

logging.basicConfig(level=logging.INFO)

def login(username):

    logging.info(f"Login attempt: {username}")

    if username == "":
        logging.error("Username missing")
        return

    logging.info("Login successful")

login("yasir")  # Output: INFO:root:Login attempt: yasir
login("")       # Output: INFO:root:Login attempt: 
                #         ERROR:root:Username missing
