from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
   <form action="/action_page" method="post"> 
   <label for="rot">
  rot: <input type="text" name="nums"/><textarea name="text">{0}</textarea>
  </label>
  <input type="submit" value="Submit"/>
</form>
    </body>
</html>
"""
@app.route("/action_page", methods=['POST'])
def program():
    text= request.form['text']
    rot= int(request.form['nums']) 
    rotted= rotate_string(text, rot)
    content = form.format(rotted)
    return content

@app.route("/")
def index():
    content = form.format('')
    return content

app.run()