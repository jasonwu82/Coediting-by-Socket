from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room, rooms
import redis
import os


#r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
r = redis.from_url(os.environ.get("REDIS_URL"), decode_responses=True)

app = Flask(__name__)
socketio = SocketIO(app)
msg_count = 0


@app.route("/")
def indexed():
    return render_template('index.html')


@app.route('/<path:path>')
def catch_all(path):
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


@socketio.on('join_room', namespace='/test')
def join_by_path(message):
    path = message['path']
    print(path)
    app.logger.error('join_room with path: %s' % path)
    join_room(path)
    if r.exists(path):
        content = r.get(path)
        emit('edit_main_response', {'data': content}, room=path)


@socketio.on('edit_main', namespace='/test')
def main_edit(message):
    global msg_count
    msg_count += 1
    app.logger.error("edit_main!!")
    app.logger.error(message['path'])
    app.logger.error(message['data'])
    emit('my_response', {'data': message['data'], 'count': msg_count}, broadcast=True)
    print(rooms())
    for room in rooms():
        emit('edit_main_response', {'data': message['data']}, room=room)
    r.set(message['path'], message['data'])



