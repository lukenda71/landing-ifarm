from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/video', methods=['POST'])
def video():
    nome_promoter = request.form['nome_promoter']
    cognome_promoter = request.form['cognome_promoter']
    nome_ospite = request.form['nome_ospite']
    return render_template("video.html",
                           nome_promoter=nome_promoter,
                           cognome_promoter=cognome_promoter,
                           nome_ospite=nome_ospite)
