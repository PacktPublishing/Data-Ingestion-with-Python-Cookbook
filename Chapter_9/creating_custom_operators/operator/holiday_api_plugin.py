from airflow.settings import AIRFLOW_HOME
from airflow.models.baseoperator import BaseOperator

import requests
import json


file_output_path = f"{AIRFLOW_HOME}/files_to_test/output_files/"

class HolidayAPIIngestOperator(BaseOperator):
    def __init__(self, filename, secret_key, country, year, **kwargs):
        super().__init__(**kwargs)
        self.filename = filename
        self.secret_key = secret_key
        self.country = country
        self.year = year

    def execute(self, context):
        params = { 'key': self.secret_key,
                'country': self.country,
                'year': self.year
        } 

        url = "https://holidayapi.com/v1/holidays?"

        output_file = file_output_path + self.filename

        try:
            req = requests.get(url, params=params)
            print(req.json())
            with open(output_file, "w") as f:
                json.dump(req.json(), f)
            return "Holidays downloaded successfully"
        except Exception as e:
            raise e