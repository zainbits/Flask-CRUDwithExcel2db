from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
load_dotenv()


engine = create_engine(os.getenv('SQLALCHEMY_DATABASE_URI'))

default_columns = {
    'Quant ID': 'id',
    'Name': 'name',
    'Title': 'title',
    'Group': 'groupname',
    'Reporting Manager': 'reporting_manager',
    'Project': 'project'
}
