from flask import Flask, render_template
from prometheus_metrics import setup_metrics
app = Flask(__name__)
setup_metrics(app)

@app.route('/')
def hello_world():
    return render_template('main.html')
#route to new_page
@app.route('/new_page')
def new_page():
    return render_template('new_page.html')
@app.route('/new_page2')
def new_page2():
    return render_template('new_page2.html')
@app.route('/new_page3')
def new_page2():
    return render_template('new_page3.html')



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')