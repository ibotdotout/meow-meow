import os
from flask import Flask
from meow_meow.render import index

app = Flask(__name__)


@app.route('/')
def render():
    print(dir(index))
    html = index.render()
    return html

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
