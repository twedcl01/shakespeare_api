#!/usr/bin/env python
"""Data models"""

from config import db, ma


class Play(db.Model):
    __tablename__ = "PLAY"
    play_id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    text = db.Column(db.String)


class PlaySchema(ma.ModelSchema):
    class Meta:
        model = Play
        sqla_session = db.session

db.create_all()