from flask import Flask, render_template, session, redirect, url_for, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# initializing default dictionnary for global variables accessible within the pages
dico = {"app_name":"Madley Sk."}

#initializing routes variable for title purpose
# routes_list=["index","chef_lieu","lieux_historiques","divisions","ressources","contact"]
routes_list={"index":"Home","chef_lieu":"County","lieux_historiques":"Historic Places","divisions":"Administrative division","ressources":"Ressources","contact":"Contact us"}

@app.route('/')
def index():
	title = "Home"
	return render_template("index.html",dico=dico,title=title)

# dealing with direct links with page extentions
@app.route('/<string:page>')
def pages(page):
	title = "Home"
	if(page):
		page = page.split(".")[0]
		if ( page in routes_list):
			title = routes_list[page]
			return render_template(page+".html",dico=dico,title=title)
	return render_template(page+".html",dico=dico,title=title)
#	return "Page not exist !", 404

@app.route('/chef_lieu')
def chef_lieu():
	title = "County"
	return render_template("chef_lieu.html",dico=dico,title=title)

@app.route('/lieux_historiques')
def lieux_historiques():
	title = "Historic Places"
	return redirect('/ressources')
#	return render_template("lieux_historiques.html",dico=dico,title=title)
	
@app.route('/divisions')
def divisions():
	title = "Territory Divisions"
	return render_template("divisions.html",dico=dico,title=title)
	
@app.route('/ressources')
def ressources():
	title = "Ressources"
	return render_template("ressources.html",dico=dico,title=title)
	
@app.route('/contact', methods=['GET','POST'])
def contact():
	title = "Contact"
	opts = ["General","Comments","Request","Information"]
	return render_template("contact.html",dico=dico,title=title,opts=opts)

@app.errorhandler(Exception)
def handle_exception(e):
	# pass through HTTP errors
	if isinstance(e, HTTPException):
		return e
	# now you're handling non-HTTP exceptions only
	return render_template("500_generic.html", e=e), 500
