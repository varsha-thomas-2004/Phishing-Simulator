from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

with app.test_request_context():
    print(url_for('hello'))

if __name__ == "__main__":
    app.run(debug=True)