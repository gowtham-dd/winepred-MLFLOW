from WinePredMLflow import logger
from WinePredMLflow.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME="Data Ingestion stage"


try:
    logger.info(f">>>> Stage {STAGE_NAME} started")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed")

except Exception as e:
    logger.exception(e)
    raise e