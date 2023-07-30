from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'welcome to the flask'

@app.route('/cal', methods =['Get'])
def math_operations():
    operation = request.json['operation']
    num_1 = request.json['num_1']
    num_2 = request.json['num_2']
    
    if operation == 'add':
        result = num_1+num_2
    elif operation == 'multiply' :
        result = num_1*num_2
    elif operation == 'division':
        result = num_1/num_2
    else :
        result = num_1-num_2
if __name__=='__main__':
    app.run()