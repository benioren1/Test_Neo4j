from flask import Flask
from blu_printes.load_data_routes import bp_load
from blu_printes.queries_routes import bp_query
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


app.register_blueprint(bp_load)

app.register_blueprint(bp_query)

if __name__ == '__main__':
    app.run()
