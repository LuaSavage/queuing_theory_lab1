from pathlib import Path
import os
import json
from basic_analysis.type import DistributionType
from view import ParamView

class Storage:

    def __init__(self,path=None) -> None:
        self.load(path=path)

    def set_file_path(self, path):
        self.file_path = Path(path+"/data.json")   

    def load(self, path=None):
        data = {}

        if path:
            self.set_file_path(path)

        if self.file_path.is_file():          
            with open(self.file_path) as json_file:
                data = json.load(json_file)
        self.data = data
        return self.data

    def save(self):
        with open(self.file_path, 'w') as outfile:
            outfile.write(json.dumps(self.data, indent=4))

    def visualise_data(self, params_dto = None):
        alias = DistributionType.get(params_dto) if params_dto else None
        print("\n")
        for key, value in (self.data).items():
            if (type(alias) == type(None)) or ((type(alias) == str) and alias == key):
                print(f"Распределение: "+key)
                for i, row in enumerate(value):
                    print(f"№ {i};",ParamView.get(row))

    def get_data (self, params_dto, row_id):
        distribution_alias = DistributionType.get(params_dto)        
        rows = self.data.get(distribution_alias, [])

        if len(rows) > row_id:
            searched_row = rows[row_id]

            #params_dto = type(params_dto)(**searched_row) 
            for prop, value in searched_row.items():
                params_dto.__setattr__(prop, value)
            return params_dto

    def add_data (self, params_dto):
        distribution_alias = DistributionType.get(params_dto) 
        if not(self.data.get(distribution_alias, False)):
            self.data[distribution_alias] = []

        self.data[distribution_alias].append(vars(params_dto))    
        return self.data 
