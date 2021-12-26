from flask import Flask, redirect, render_template,session,request

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


if __name__ == '__main__' :
    app.run(debug=True)


