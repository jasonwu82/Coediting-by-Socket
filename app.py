from flask import Flask, render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)
socketio = SocketIO(app)
msg_count = 0


@app.route("/")
def indexed():
    return render_template('index.html')


@socketio.on('my_event', namespace='/test')
def chat_msg(message):
    global msg_count
    msg_count += 1
    emit('my_response', {'data': message['data'], 'count': msg_count})


@socketio.on('connect', namespace='/test')
def test_connect():
    app.logger.error("connecting!!")
    emit('my_response', {'data': 'Connected!'})


@socketio.on('edit_main', namespace='/test')
def test_connect(message):
    global msg_count
    msg_count += 1
    app.logger.error("edit_main!!")
    app.logger.error(message['data'])
    emit('my_response', {'data': message['data'], 'count': msg_count}, broadcast=True)
    emit('edit_main_response', {'data': message['data']}, broadcast=True)



