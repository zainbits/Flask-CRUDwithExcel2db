from flask_restplus import Resource
from flask import request

from quants.common import engine, default_columns
from sqlalchemy import text
import pandas as pd


class Upload(Resource):
    def post(self):
        if request.method == "POST":
            f = request.files['file']
            data_xlsx = pd.read_excel(f)
            data_xlsx = data_xlsx[default_columns.keys()]
            data_xlsx.rename(columns=default_columns, inplace=True)

            data = data_xlsx.T.to_dict().values()

            with engine.connect() as con:
                query = text("""INSERT INTO qusers (id, name, title, groupname, reporting_manager, project) values (:id, :name, :title, :groupname, :reporting_manager, :project) ON CONFLICT (id) DO UPDATE SET name=:name, title=:title, groupname=:groupname, reporting_manager=:reporting_manager, project=:project""")
                for line in data:
                    con.execute(query, **line)

            return data_xlsx.to_html()

        # df = pd.read_sql_table('qusers', engine)
        return 'out of post'

    def get(self):
        df = pd.read_sql_table('qusers', engine)
        return df.to_html()
