from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'welcome to the flask'

if __name__=='__main__':
    app.run()