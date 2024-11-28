from flask import Flask
from blu_printes.load_data_routes import bp_load
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


app.register_blueprint(bp_load)  # add the blueprint to the Flask app

if __name__ == '__main__':
    app.run()
