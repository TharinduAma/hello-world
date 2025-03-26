# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)


# in hello_flask.py
@app.route('/')
def acronym():
   return '<p>Genevieve M. : afaik</p>' \
   '<p>Tanner C. : idk</p>' \
   '<p>Jhon D. : EOD</p>'

@app.route('/tharindu')
def my_acronym():
    return render_template('template.html')

