import os
from pydantic import PostgresDsn
from pydantic_settings  import BaseSettings
class Config(BaseSettings):
   host: PostgresDsn

   class Config:
       env_prefix = "db_"