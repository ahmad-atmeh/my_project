from flask import Flask , render_template
import random
me = {
	"first_name":"Allan",
	"last_name":"Turing",
	"descial_links": [
			{"site":"Twitter","url":"https://twitter.com/someone"}, 
			{"site": "GitHub", "url": "https://github.com/someone"}
	],
	"age": 25,
	"avatarURL": "https://somewebsite.com/someusername/myprofile.jpg",
	"email": "you@email.com",
	"skills": ["Python", "Flask", "JavaScript", "HTML"],
	"projects": [
		{"name":"Tic-Tac-Toe", "description":"A description for the project.", "tags":["functions", "control structures", "game"]},
		{"name":"Battle of Teams", "description":"A description for the project.", "tags":["functions", "OOP"]},
		{"name":"Resume", "description":"A description for the project.", "tags":["flask", "web application", "HTTP routes"]}
	],
	"favourite_quotes": [
		{"quote":"Patience you must have my young Padawan.", "author":"Yoda"},
		{"quote":"The more a thing tends to be permanent, the more it tends to be lifeless.", "author":"Alan Watts"},
		{"quote":"Logic will get you from A to Z; imagination will get you everywhere.", "author":"Albert Einstein"}
	]
}


app = Flask(__name__)

@app.route('/')
def render_index():
    full_name=me["first_name"] + " " + me["last_name"]

    return render_template("index.html",full_name=full_name)
	

