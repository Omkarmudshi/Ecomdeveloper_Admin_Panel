import logging
import os
class LogGen:
    @staticmethod
    def logger():
        logging.basicConfig(filename=r"Logs\automation.log",format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m%d%Y %I%M%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


# class LogGen:
#     @staticmethod
#     def logger():
#         log_directory = "Logs"
#         if not os.path.exists(log_directory):
#             os.makedirs(log_directory)

#         logging.basicConfig(
#             filename=os.path.join(log_directory, "automation.log"),
#             format='%(asctime)s: %(levelname)s: %(message)s',
#             datefmt='%m%d%Y %I:%M:%S %p'
#         )
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger