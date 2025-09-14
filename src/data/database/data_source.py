import os
from dotenv import load_dotenv
from src.data.database.data_source_mysql import DataSourceMySQL
from src.data.database.data_source_postgre import DataSourcePostgre

load_dotenv()

class DataSource:
    def __init__(self):
        self.datasource_name = os.getenv("CURRENT_DATA_SOURCE", "mysql")
        self.ds = self._get_ds_instance()

    def _get_ds_instance(self):
        sources = {
            "mysql": DataSourceMySQL,
            "postgre": DataSourcePostgre
        }
        ds_class = sources.get(self.datasource_name.lower())
        if ds_class is None:
            raise ValueError(f"Data source '{self.datasource_name}' no soportado")
        return ds_class()

    def get_data_source(self):
        return self.ds

# Dependencia para obtener la sesión de la base de datos
def get_db():
    ds_instance = DataSource().get_data_source()
    db = ds_instance.get_session()
    
    try:
        yield db
    finally:
        db.close()