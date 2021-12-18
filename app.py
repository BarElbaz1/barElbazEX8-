from flask import Flask, redirect, render_template, request, session

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
    if __name__ == '__main__':
        app.run(debug=True)
