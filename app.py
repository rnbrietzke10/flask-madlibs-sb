from flask import Flask, request, render_template
from stories import story

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickenzarecool21837"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page(): 
    """Shows home page"""
    words = story.prompts
    return render_template('home.html', words = words)


@app.route('/story')
def story_page():
    user_words = request.args
    text = story.generate(user_words)
    return render_template('story.html',text = text)
