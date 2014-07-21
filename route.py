import os
from flask import Flask
from meow_meow.render import index

app = Flask(__name__)
app.config['DEBUG'] = os.environ.get('DEBUG', False)


@app.route('/')
def render():
    return index.render()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
