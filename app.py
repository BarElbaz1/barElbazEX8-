from flask import Flask, redirect, render_template, session, request, jsonify

from interact_with_DB import interact_db
from flask import jsonify
import requests
import random



app = Flask(__name__)
app.secret_key = '123'


@app.route('/CV')
@app.route('/')
def index():
    return render_template('CV.html')


@app.route('/CVgrid')
def mycv():
    return render_template('CVgrid.html')


@app.route('/TV_shows')
def tv():
    return render_template('TV_shows.html')


@app.route('/assigment8')
def assigment8():
    return render_template('assigment8.html',
                           user={'firstname': "Bar", 'lastname': "Elbaz"},
                           hobbies=['going to the beach', 'play piano', 'hang out with friends'])


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    username = ''
    users = [{'id': 1, 'email': "yael.golan@reqres.in", 'firstname': "yael", 'lastname': "golan"},
        {'id': 2, 'email': "carmel.berko@reqres.in", 'firstname': "carmel", 'lastname': "berko"},
        {'id': 3, 'email': "zohar.dardik@reqres.in", 'firstname': "zohar", 'lastname': "dardik"},
        {'id': 4, 'email': "gal.elbaz@reqres.in", 'firstname': "gal", 'lastname': "elbaz"},
        {'id': 5, 'email': "dana.rubin@reqres.in", 'firstname': "dana", 'lastname': "rubin"},
        {'id': 6, 'email': "hadas.gal@reqres.in", 'firstname': "hadas", 'lastname': "gal"}]
    firstname = ''
    logged_in = True

    if request.method == 'GET':
        if 'firstname' in request.args:
            firstname = request.args['firstname']

    if request.method == 'POST':
        username = request.form['username']
        session['logged_in'] = True
        session['username'] = username
    return render_template('assignment9.html',
                           request_method=request.method,
                           name=firstname,
                           users=users,
                           username=username)


@app.route('/log_out')
def log_out():
    session.pop('username')
    session['logged_in'] = False
    session['username'] = ''
    return redirect('/assignment9')


from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)



@app.route('/assignment11')
def assignment11_fun():
    return render_template('assignment11.html')


## assignment 11
@app.route('/assignment11/users')
def assignment11_users_fun():
    return_dict = {}
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    for user in users:
        return_dict[f'user_{user.id}'] = {
            'status': 'success',
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        }
    return jsonify(return_dict)


@app.route('/assignment11/outer_source')
def assignment11_outer_source_fun():
    return render_template('request_outer_source.html')


def get_user(id):
    if (id != ""):
        user_id = int(id)
        return requests.get(f'https://reqres.in/api/users/{user_id}').json()

    users = []
    length = len(requests.get(f'https://reqres.in/api/users').json()['data'])

    for i in range(1, length+1):
        res = requests.get(f'https://reqres.in/api/users/{i}')
        res = res.json()
        users.append(res)
    return users


@app.route('/req_backend')
def req_backend():
    if "user_id" in request.args:
        user_id = request.args['user_id']
        if user_id == "":
            users = get_user(user_id)
            return render_template('request_outer_source.html', users=users)
        else:
            user = get_user(user_id)
            return render_template('request_outer_source.html', user=user)

    return render_template('request_outer_source.html')

if __name__ == '__main__' :
    app.run(debug=True)


