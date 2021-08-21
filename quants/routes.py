from quants import api
from quants.upload.exceldb import Upload
from quants.users.resources.quantsres import Quants


api.add_resource(Quants, '/users')
api.add_resource(Quants, '/users/update/<string:quant_id>')
api.add_resource(Upload, '/upload')
api.add_resource(Quants, '/users/delete/<string:quant_id>')
