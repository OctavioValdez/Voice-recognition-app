from flask import Flask, jsonify, request
from controller import Controller
from flask_cors import CORS


app = Flask(__name__)
controller = Controller()
CORS(app)

@app.route('/')
def hello_world():
    return '<p>Hello World</p>'

@app.route('/artist', methods=['GET'])
def get_artist():
    artist_name = request.args.get('name')
    data = controller.get_artist_controller(artist_name)
    return data

@app.route('/track', methods=['GET'])
def get_track():
    track_name = request.args.get('name')
    data = controller.get_track_controller(track_name)
    return data


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")