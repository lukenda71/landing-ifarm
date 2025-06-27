from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)

# Dizionario per memorizzare i dati temporaneamente
user_data = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome_promoter = request.form.get('nome_promoter')
    cognome_promoter = request.form.get('cognome_promoter')
    nome_ospite = request.form.get('nome_ospite')
    regione_ospite = request.form.get('regione_ospite')

    # Genera ID univoco breve
    unique_id = str(uuid.uuid4())[:8]

    # Salva dati
    user_data[unique_id] = {
        'nome_promoter': nome_promoter,
        'cognome_promoter': cognome_promoter,
        'nome_ospite': nome_ospite,
        'regione_ospite': regione_ospite
    }

    return redirect(url_for('video', uid=unique_id))

@app.route('/video/<uid>')
def video(uid):
    if uid in user_data:
        dati = user_data[uid]
        return render_template('video.html', **dati)
    else:
        return "Link non valido o scaduto", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)