import os, sys
from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException


from cellSegmentation.pipeline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()

print('Training Completed.')

