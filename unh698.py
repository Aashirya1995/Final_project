from flask import Flask
app = Flask(__name__)
#UNH698 py file
@app.route('/')
def hello_world():
    return 'UNH698 Website'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)
    #port 8080