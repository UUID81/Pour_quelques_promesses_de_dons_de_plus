from flask import Flask, render_template, request
import data

app = Flask(__name__)


@app.route('/')
def index() :
    return render_template('index.html')

@app.route('/form')
def form(): 
     return render_template('form.html' )

@app.route('/Merci pour votre don')
def merci():
    return render_template('merci.html')

@app.route('/fiche')
def fiche():
    donnateur = data.get_donnateurs()
    total= data.total_dons()
    return render_template('fiche.html', quelquun=donnateur, total=total)


@app.route('/add', methods=['GET'])
def add():
    nom = request.values.get('nom')  
    prenom = request.values.get('prenom')
    don = request.values.get('don')

    data.set_donnateurs(nom, prenom, don)
    
    return render_template('add.html')

if __name__== "__main__" :
    app.run(debug=True, port=5001)