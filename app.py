from flask import Flask, jsonify, make_response
from flask import render_template
from config import app
from models import Play, PlaySchema
from build_db import build_db

build_db("complete_works")



@app.route("/")
def show_table():
    complete_works = Play.query.all()
    play_schema = PlaySchema(many=True)
    return "Please Search for a word!"


@app.route("/search_for_<word>/", methods=['GET'])

def searchForWord(word):
	texts = Play.query.with_entities(Play.text)
	full_text = ''
	for text in texts:
		print(text.text)
		full_text += text.text
	count = full_text.count(word)
	return jsonify({"count": count})


@app.route("/search_for_<word>_in_<play>", methods=['GET'])

def searchForWordInPlay(word, play):
	work = Play.query.filter_by(play_id=play).first()
	text = work.text
	count = int(text.count(word))
	return jsonify({"count": count})

if __name__ == '__main__':
   app.run(debug = True)