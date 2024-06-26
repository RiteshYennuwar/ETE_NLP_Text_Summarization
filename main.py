from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.logging import logger

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'_-_-_->>> stage {STAGE_NAME} started <<<-_-_-_')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'_-_-_-<<< stage {STAGE_NAME} completed >>>-_-_-_')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Validation Stage'

try:
    logger.info(f'_-_-_->>> stage {STAGE_NAME} started <<<-_-_-_')
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f'_-_-_-<<< stage {STAGE_NAME} completed >>>-_-_-_')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Transformation Stage'

try:
    logger.info(f'_-_-_->>> stage {STAGE_NAME} started <<<-_-_-_')
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f'_-_-_-<<< stage {STAGE_NAME} completed >>>-_-_-_')
except Exception as e:
    logger.exception(e)
    raise e