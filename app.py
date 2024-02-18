from flask import Flask, render_template

app = Flask(__name__)

site_name="Praudexai"

@app.route('/', methods=['GET'])
def auth_page():
    return render_template('auth.html', site_name=site_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


