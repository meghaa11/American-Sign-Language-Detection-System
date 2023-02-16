from flask import Flask, render_template
#import libraries

app = Flask(__name__) #initialise app

@app.route("/")     #decotor
def index():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return "Hello, World!"


if __name__=="__main__":
    app.run()

'''
$flask_final
│   ├── index.py
│   │   ├── static
│   │   |   ├── style.css
│   │   |   ├── any images or files
│   │   └── template
│   │   │   └── index.html
    '''