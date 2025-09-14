import os
from dotenv import load_dotenv
from src.data.database.data_source_mysql import DataSourceMySQL
from src.data.database.data_source_postgre import DataSourcePostgre

load_dotenv()

class DataSource:
    def __init__(self):
        self.datasource_name = os.getenv("CURRENT_DATA_SOURCE", "mysql")

    def get_data_source(self):
        sources = {
            "mysql": DataSourceMySQL,
            "postgre": DataSourcePostgre
        }

        ds_class = sources.get(self.datasource_name.lower())
        if ds_class is None:
            raise ValueError(f"Data source '{self.datasource_name}' no soportado")

        return ds_class()
