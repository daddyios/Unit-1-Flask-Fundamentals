
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', method = {"GET",'POST'})
def hello():
    return render_template('home.html')


@app.route('/profile/<username>')
def profile(username):
    user_data = {
        'name':username,
        'school':'BT',
        'age': 16,
        'is_present':True
    }
    return render_template("profile.html", user=user_data)

@app.route('/contact',method={"GET","POST"})
def contact(contact):
    if request.method == 'GET':
        return render_template("profile.html", user=contact)
    elif request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

if __name__ == '__main__':
    app.run(debug=True)



