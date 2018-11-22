from flask import Flask
from flask import *
from database import *
from flask import Flask, render_template, url_for , request ,session, escape, request, redirect


app = Flask(__name__)

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/addcat', methods=['GET' , 'POST'])
def Add_cat():
	if request.method== 'GET':
		return render_template('makecat.html')
	else:
		catname = request.form['txb_addcat']
		create_cat(catname)
		return redirect(url_for('catbook_home'))


@app.route('/cats/<int:id>')
def catbook_profile(id):
	get_cat_by_id(id)
	return render_template("cat.html",)


if __name__ == '__main__':
   app.run(debug = True)
