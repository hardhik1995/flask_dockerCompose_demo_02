from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    
    return 'Hello world! I am Hardhik dash & Demo is working'

if __name__ == '__main__':
    
    app.run(host='0.0.0.0')

