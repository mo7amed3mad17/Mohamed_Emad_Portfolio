from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('Home.html')

@app.route('/education')
def education():
    return render_template('Education_&_Skills.html')

@app.route('/portfolio')
def portfolio():
    return render_template('Portfolio.html')

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/contact')
def contact():
    return render_template('Contact.html')


if __name__ == '__main__':
    app.run(debug=True)