from flask import Flask
from flask import render_template 
from database import get_all_cats , get_cat_by_id
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
		catname = request.form("txb_addcat")
		createcat(catname)
		return render_template('home.html')


@app.route('/cats/<int:id>')
def catbook_profile(id):
	get_cat_by_id(id)
	return render_template("cat.html",)


if __name__ == '__main__':
   app.run(debug = True)
