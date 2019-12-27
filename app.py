from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def index0():
    return render_template('index.html')

@app.route('/timeline.html')
def index1():
	return render_template('timeline.html')

@app.route('/gallery.html')
def index2():
	return render_template('gallery.html')

@app.route('/portfolio.html')
def index3():
	return render_template('portfolio.html')

@app.route('/contact.html')
def index4():
	return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)