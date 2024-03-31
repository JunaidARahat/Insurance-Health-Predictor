from collections import namedtuple
from datetime import datetime
import uuid
from insurance.config.configuration import Configuartion
from insurance.logger import logging, get_log_file_name
from insurance.exception import InsuranceException
from threading import Thread
from typing import List

from multiprocessing import Process

from insurance.entity.artifact_entity import DataIngestionArtifact
from insurance.components.data_ingestion import DataIngestion

import os, sys
from collections import namedtuple
from datetime import datetime
import pandas as pd



class Pipeline(Thread):
    pass

    def __init__(self, config: Configuartion) -> None:
        try:
            os.makedirs(config.training_pipeline_config.artifact_dir, exist_ok=True)

        
            super().__init__(daemon=False, name="pipeline")
            self.config = config
        except Exception as e:
            raise InsuranceException(e, sys) from e
        
    

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise InsuranceException(e, sys) from e
        



    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        

        except Exception as e:
            raise InsuranceException(e, sys) from e
    
    def run(self):
        try:
            self.run_pipeline()
        except Exception as e:
            raise e


