from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
    <form method="POST">
        <label for="rot">Rotate by:</label>
        <input type="text" name="rot" value="0">
        <br>
        <textarea name="text" value=""></textarea>
        <input type="submit" value="Submit">
    </form>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    result = rotate_string(text, rot)
    form = """
        <!DOCTYPE html>
            <body>
            <h1>{0}</h1>
            </body>
        </html>
    """
    return form.format(result)

@app.route("/")
def index():
    return form

app.run()