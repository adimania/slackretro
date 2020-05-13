from flask import Flask, request
import slack
import datetime
import os
from app import app, db
from  app.models import Channel

@app.route("/isup")
def isup():
    Channel.query.limit(1).all()
    return 'up'

@app.route("/slack/addretro", methods=['GET', 'POST'])
def add_retro():
    if request.method == 'POST':
        incoming = request.form['text']
        if request.form['text'] == "":
            return 'I cannot add empty lines to the retro.'
        channel = Channel(userid=request.form['user_id'], channel=request.form['channel_id'], message=request.form['text'])
        db.session.add(channel)
        db.session.commit()
    return 'OK. I added your item to the retro.'

@app.route("/slack/getretro", methods=['GET', 'POST'])
def get_retro():
    if request.method == 'POST':
        if request.form['text'].split()[0] == 'since' and validate_date(request.form['text'].split()[1]):
            retro = Channel.query.filter_by(channel=request.form['channel_id']).filter(Channel.timestamp >= request.form['text'].split()[1]).all()
            if len(retro) == 0:
                return ('There are no items for the retro.')
            response = ""
            for message in retro:
                response = response + "• [ <@{!s}> ] {!s}\n".format(message.userid, message.message)
            slack_token = os.environ["SLACK_API_TOKEN"]
            client = slack.WebClient(token=slack_token)
            client.chat_postMessage(channel=request.form['channel_id'], text=response)
            return ('', 204)
    return ('I do not understand this. May be try again later.', 200)

def validate_date(date_string):
    date_format = '%Y-%m-%d'
    try:
        date_obj = datetime.datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        client.chat_postMessage(channel=request.form['channel_id'], text="I do not understand this date format: `date_string`. Please use yyyy-mm-dd.")
