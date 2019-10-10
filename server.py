from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    # socketio.run(app, debug=True,host = '127.0.0.1',port = 8089)
    socketio.run(app, debug=True)


# from flask_socketio import SocketIO, send
# from flask import Flask
# application = Flask(__name__)
# socketio = SocketIO(application)

# @socketio.on('')

# @socketio.on('message')
# def doStuff(msg):
#     print(msg)
#     send("sent from server...")

# if __name__=="__main__":
#   socketio.run(application,host = '127.0.0.1',debug=True, port=8090)
# print("server hosted")