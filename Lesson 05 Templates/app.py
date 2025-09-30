
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



