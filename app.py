from flask import Flask, redirect, session, render_template, request
from flask_session import Session
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(128)


@app.route('/')
def hello_world():
    token = session.get('token', '')
    if token == '':
        return redirect('/login')
    else:
        return redirect('/hi')


@app.route('/login', methods=['GET', 'POST'])
def route_login():
    if request.method == 'POST':
        session.pop
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return redirect('/login-results')

    context = {
        'username': svar('username'),
        'password': svar('password')
    }
    return render_template('login.html', context=context)


def svar(name):
    result = session.get(name)
    if result is None:
        result = ''
    return result

@app.route('/login-results')
def route_login_results():
    context = {
        'username': session.get('username',''),
        'password': session.get('password','')
    }
    return render_template('login-results.html', context=context)

@app.route('/hi')
def route_hi():
    s = '''
    <h1>
    Hi This is a web page.
    <button>hello</button>
    </h1>
    '''
    response = make_response(s)
    response.set_cookie('a cookie from app', '12345')
    return response


if __name__ == '__main__':
    app.run()
