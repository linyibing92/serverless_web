
from flask import Flask, render_template

app = Flask(__name__, static_folder="../vue-admin-template/dist/static", template_folder="../vue-admin-template/dist")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

