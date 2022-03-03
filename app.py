from flask import Flask, send_from_directory
from main.main import main_blueprint
from loader.loader import loader_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024


@app.route('/main/static/<path:path>')
def static_dir(path):
    return send_from_directory('main/static', path)


@app.route('/loader/static/<path:path>')
def static_dir_loader(path):
    return send_from_directory('loader/static', path)


@app.route('/uploads/<path:path>')
def static_dir_uploads(path):
    return send_from_directory('uploads', path)
