from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'A secret makes a woman woman'


@app.route('/')
def index():
    if 'activities' not in session:
        session['activities'] = []
    if 'gold_amt' not in session:
        session['gold_amt'] = 0
    if 'moves' not in session:
        session['moves'] = 15
    if 'display' not in session:
        session['display'] = 'none'
    return render_template("index.html", gold_amt=session['gold_amt'], activities=session['activities'], moves=session['moves'], display=session['display'])

@app.route('/process_money', methods=['POST'])
def process_money():
    dt_string = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    gold_generator = {
        'farm': random.randint(10, 20),
        'cave': random.randint(5, 10),
        'house': random.randint(2, 5),
        'casino': random.randint(-50, 50),
    }
    location = request.form["location"]
    session['gold_amt'] += gold_generator[location]

    if gold_generator[location] < 0:
        session['activities'].append(
            f"<p style='color: red'> Earned {gold_generator[location]} from the {location}! ({dt_string}) </p>")
    else:
        session['activities'].append(
            f"<p style='color: green'> Earned {gold_generator[location]} from the {location}! ({dt_string}) </p>")

        session['moves'] -= 1
        if session['moves'] == 0 or session['gold_amt'] >= 500:
            session['display'] = 'inline-block'
    return redirect("/")


@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
