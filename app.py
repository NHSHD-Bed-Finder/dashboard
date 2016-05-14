import os

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/units')
def units():
    return render_template('units.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(
        host="0.0.0.0",
        port = port,
        debug=True
    )