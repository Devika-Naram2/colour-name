from flask import Flask
import os
from termcolor import colored


app = Flask(__name__)

@app.route('/')
def hello():
    print colored('hello', 'red'), colored('world', 'green')
    return "Hello DTI team. This is REDHAT demo"


if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
