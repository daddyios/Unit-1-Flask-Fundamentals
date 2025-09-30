app = flask(__name__)

@app.route('/')
def hello():
    return '''
        <a href="/feedback"> Feedback Form </a>

'''

app.route("/feedback",methods = {'GET',"POST"})
def feedback():
    if request.method=='POST':
        name=request.args.get('name')
    return render_template('form.html')