from flask import Flask, render_template, request

app = Flask(__name__)

# ✅ Funzione per validare il codice
def is_valid_code(code):
    return len(code) == 6 and code.count('1') >= 1

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/video', methods=['POST'])
def video():
    nome_promoter = request.form['nome_promoter']
    cognome_promoter = request.form['cognome_promoter']
    nome_ospite = request.form['nome_ospite']
    codice = request.form['codice']

    if not is_valid_code(codice):
        return "Codice non valido. Deve essere di 6 cifre e contenere almeno una '1'.", 400

    return render_template("video.html",
                           nome_promoter=nome_promoter,
                           cognome_promoter=cognome_promoter,
                           nome_ospite=nome_ospite)
