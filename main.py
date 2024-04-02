from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.logging import logger

STAGE_NAME = 'Data Ingestion stage'

try:
    logger.info(f'_-_-_->>> stage {STAGE_NAME} started <<<-_-_-_')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'_-_-_->>> stage {STAGE_NAME} completed <<<-_-_-_')
except Exception as e:
    logger.exception(e)
    raise e