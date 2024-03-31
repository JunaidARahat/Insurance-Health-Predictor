from insurance.pipline.pipline import Pipeline
from insurance.config.configuration import Configuartion
from insurance.constants import get_current_time_stamp



obj=Pipeline(config=Configuartion(current_time_stamp=get_current_time_stamp()))
obj.run_pipeline()