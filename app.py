from flask import Flask, request, render_template

app = Flask(__name__)

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route('/')
def index():
    return render_template('index.html', messages = messages)

@app.route('/usuario/<name>')
def user(name):
    return render_template("user.html", user = name)  

@app.route('/usuario')
def user_incognito():
    return render_template('user.html')

@app.route('/navegador')
def browser():
    user_agent = request.headers.get('User-Agent')
    return f"tu naegador es: {user_agent}"

@app.route('/rutas')
def routes():
    print(app.url_map)
    return "revisa tu consola para ver las rutas"    

@app.errorhandler(404)
def page_not_found(error):
  return render_template('page_not_found.html'), 400          