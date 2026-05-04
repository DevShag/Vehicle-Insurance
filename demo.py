from src.logger import logging
from src.pipeline.training_pipeline import TrainPipeline

"""
logging.debug("This is a debug message")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")
"""

pipline = TrainPipeline()
pipline.run_pipeline()

