from flask import Flask, render_template 
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

@app.route('/')
def hello():
  return "<p>Silvia J.: IDK</p>"

@app.route('/jessika')
def wc():
   s1 = 'Favorite acronym: '
   s2 = 'LOL'
   return s1 + s2

@app.route('/mytemplate')
def t_test():
   return render_template('my_template_1.html')

bootstrap = Bootstrap5(app)