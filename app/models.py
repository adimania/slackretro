from app import db
from datetime import datetime, time

class Channel(db.Model):
    id = db.Column(db.Integer, primary_key = True) #, autoincrement=True)
    userid = db.Column(db.String(80), index=True)
    channel = db.Column(db.String(80), index=True)
    message = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    nature = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return '<Channel: {}, User: {}, Message: {}>'.format(self.channel, self.userid, self.message)
