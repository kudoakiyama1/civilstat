from datetime import datetime

from civilstat import db


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname_id = db.Column(db.Integer, db.ForeignKey("fullname.id"), nullable=False)
    sex = db.Column(db.String(8), nullable=False)
    submitted_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Fullname(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(128), nullable=False)
    middlename = db.Column(db.String(128))
    lastname = db.Column(db.String(128), nullable=False)
    suffix = db.Column(db.String(4))

    entries = db.relationship("Entry", backref="fullname")