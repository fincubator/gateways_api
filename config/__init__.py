import yaml
from pathlib import Path
from config.const import *


project_root_dir = Path(__file__).parent.parent

cfg = yaml.safe_load(open(f"{project_root_dir}/config/config.yml", 'r'))

pg_config = cfg["postgres"]
sql_conn_url = f"postgres+psycopg2://{pg_config['user']}:{pg_config['password']}" \
               f"@" \
               f"{pg_config['host']}:{pg_config['port']}/{pg_config['database']}"
