from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/new_page')
def new_page():
    return render_template('new_page.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)