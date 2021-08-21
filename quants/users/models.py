from quants import db


class UserModel(db.Model):
    __tablename__ = 'qusers'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    groupname = db.Column(db.String, nullable=False)
    reporting_manager = db.Column(db.String, nullable=False)
    project = db.Column(db.String, nullable=False)

    def __init__(self, id, name, title, groupname, reporting_manager, project):
        self.id = id
        self.name = name
        self.title = title
        self.groupname = groupname
        self.reporting_manager = reporting_manager
        self.project = project
