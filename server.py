from flask import Flask, render_template
from sender import runner
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  print ('I got clicked')
  return f'{runner()}'

if __name__ == '__main__':
  app.run(debug=True)