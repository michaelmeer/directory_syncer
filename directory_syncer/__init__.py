from flask import Flask, render_template
from directory_syncer.config import configure_app

app = Flask(__name__)
configure_app(app)

@app.route('/')
def index():
    return render_template('main-template.html', timestamp=app.config["RSYNC_COMMAND"])
    


