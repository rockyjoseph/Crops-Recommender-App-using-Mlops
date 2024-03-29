import sys
import pandas as pd

from src.exception import CustomException
from src.utils import load_obj

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = 'artifacts/model.pkl'
            preprocessor_path = 'artifacts/preprocessor.pkl'
            model = load_obj(file_path = model_path)
            preprocessor = load_obj(file_path = preprocessor_path)
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self, 
        nitogen: int,
        phosphorus: int,
        potassium: int,
        temperature: float,
        humidity: float,
        ph: float,
        rainfall: float
    ):

        self.nitogen = nitogen
        self.phosphorus = phosphorus
        self.potassium = potassium
        self.temperature = temperature
        self.humidity = humidity
        self.ph = ph
        self.rainfall = rainfall

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                'nitrogen': [self.nitogen],
                'phosphorus': [self.phosphorus],
                'potassium': [self.potassium],
                'temperature': [self.temperature],
                'humidity': [self.humidity],
                'ph': [self.ph],
                'rainfall': [self.rainfall],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
