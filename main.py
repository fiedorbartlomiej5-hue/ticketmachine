import json
from flask import Flask, render_template, request

app = Flask(__name__)

# Wczytanie cennika z pliku prices.json
try:
    with open('prices.json', 'r', encoding='utf-8') as f:
        prices = json.load(f)
except FileNotFoundError:
    prices = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        ticket_type = request.form.get('ticket_type')
        if ticket_type in prices:
            message = f"Pomyślnie kupiono bilet: {ticket_type} (Cena: {prices[ticket_type]} zł)"
        else:
            message = "Wybrany bilet nie istnieje."

    return render_template('index.html', prices=prices, message=message)

if __name__ == '__main__':
    app.run(debug=True)