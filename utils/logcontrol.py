import time
import os


class LogControl:

    def __init__(self):
        # logs
        try:
            os.makedirs("logs", exist_ok=True)
        except OSError:
            raise

    def log(msg):
        ts = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        error = open("logs/neoscan_log.log", "a")
        error.write(ts + ": " + msg + "\n")
        error.close()