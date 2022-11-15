from web import create_app
from flask import render_template

# create a new instance of web app
app = create_app()

if (__name__ == '__main__'):
    app.run(debug=True)
