from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def home_page():
    #TODO serve yeet.html
    return 'yeet this is the home page'


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=int(os.environ.get('PORT', 8080)))
