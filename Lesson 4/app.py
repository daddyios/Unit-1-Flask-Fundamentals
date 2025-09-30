from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
           <h1>Dynamic Routes Demo</h1>
<h2>Try: These URLS</h2>
<ul>
    <li><a href="/user/john">User Profile: john</a></li>
    <li><a href="/user/alice">User Profile: alice</a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
</ul> 
"""

@app.route('/user/<username>')
def user_profile(username):
    return f'''
     <h1>User Profile</h1>
 <p>Username: <strong>{username}</strong></p>
 <p>Profile Type: {type(username).__name__}</p>
 <p>Welcome to {username}'s profile page!</p>
 <nav>
    <a href="/"> Back to Homepage</a>
    <a href="/user/alice">Alice</a>
    <a href="/user/bob">Bob</a>
 </nav>    
'''
operations = []
@app.route("/calc/<int:num1>/<operation>/<int:num2>")
def calculator(num1,operation,num2):
    if operations in operation:
        result = operations[operation]
    return f"{num1} {operation} {num2} = "
if __name__ == "__main__":
    app.run(debug=True)

@app.route("/temp/<degree>/<int: temp>")

def converter(temp, degree):
    if  degree.lower() == 'c':
        return f'''<h1>{(temp-32)*(5/9)}</h1>'''
    else:
        return f'''<h1>{temp*(9/5)+32}</h1>'''

