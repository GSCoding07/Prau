from flask import Flask, render_template

app = Flask(__name__)

site_name = "Praudexai"

@app.route('/', methods=['GET'])
def auth_page():
    return render_template('auth.html', site_name=site_name)

@app.route('/SignUp', methods=['GET'])
def signup_page():
    return render_template('su.html', site_name=site_name)

@app.route('/Login', methods=['GET'])
def Login_page():
    return render_template('login.html', site_name=site_name)

@app.route('/Premium', methods=['GET'])
def Premium_page():
    return render_template('premium.html', site_name=site_name)

@app.route('/Home', methods=['GET'])
def Home_page():
    return render_template('home.html', site_name=site_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
