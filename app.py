from flask import Flask, request, render_template


from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickenzarecool21837"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """Shows home page"""
    return render_template('home.html')