from flask import Flask, render_template, render_template_string

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'CURRENTLY UNDER CONSTRUCTION'


@app.route('/generators')
def generators_route():
    # Should probably get available generators out of a database and build links to them to zepto into the page?
    return render_template("generators.html")


@app.route('/games')
def games_route():
    return render_template("games.html")


@app.route('/games/embers')
def embers_route():
    return render_template("embers.html")


<<<<<<< HEAD
@app.route('/games/tyvm')
def tyvm_route():
    return render_template("tyvm.html")


=======
>>>>>>> origin/master
@app.route('/games/worstwizard')
def worstwizard_route():
    return render_template("worstwizard.html")

<<<<<<< HEAD
=======

@app.route('/vanessa')
def v():
    return render_template("v.html")


>>>>>>> origin/master
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
