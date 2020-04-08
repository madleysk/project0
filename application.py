from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)

dico = {"app_name":"Madley Sk."}

@app.route('/')
def index():
	title = "Accueil"
	return render_template("index.html",dico=dico,title=title)

@app.route('/chef_lieu')
def chef_lieu():
	title = "County"
	return render_template("chef_lieu.html",dico=dico,title=title)

@app.route('/lieux_historiques')
def lieux_historiques():
	title = "Historic Places"
	return render_template("lieux_historiques.html",dico=dico,title=title)
	
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
