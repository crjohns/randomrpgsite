from flask import Flask, url_for
from flask import render_template, send_from_directory, redirect, Response

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/<version>/<item>/<iid>')
def api(version, item, iid):
    if version != 'v1':
        return "Unknown api version", 500

    if item == 'js' and iid == 'client.js':
        return Response(render_template('client.js'), content_type='text/javascript')

    return 'Invalid request', 500



@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))



if __name__ == "__main__":

    app.debug = True
    app.run()
