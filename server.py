from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'A secret makes a woman woman'

activities = []

@app.route('/')
def index():
    return render_template("index.html", gold_amt=session['gold_amt'], activities = activities)

@app.route('/process_money', methods=['POST'])
def process_money():
    dt_string = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    # Farm
    if request.form['which_action'] == "farm":
        add_gold_farm = random.randint(10, 20)
        session['gold_amt'] += add_gold_farm
        activities.append(f"<p style='color: green'>Earned {add_gold_farm} from the farm! ({dt_string}) </p>")
    # Cave
    elif request.form['which_action'] == "cave":
        add_gold_cave = random.randint(5, 10)
        session['gold_amt'] += add_gold_cave
        activities.append(f"<p style='color: green'>Earned {add_gold_cave} from the cave! ({dt_string}) </p>")
    # House
    elif request.form['which_action'] == "house":
        add_gold_house = random.randint(2, 5)
        session['gold_amt'] += add_gold_house
        activities.append(f"<p style='color: green'>Earned {add_gold_house} from the house! ({dt_string})</p>")
    # Casino
    elif request.form['which_action'] == "casino":
        add_gold_casino = random.randint(-50, 50)
        session['gold_amt'] += add_gold_casino
        if add_gold_casino < 0:
            activities.append(f"<p style='color: red'>Earned {add_gold_casino} from the casino! ({dt_string}) </p>")
        else:
            activities.append(f"<p style='color: green'>Earned {add_gold_casino} from the casino! ({dt_string}) </p>")
    return redirect("/")

@app.route('/reset', methods=['POST'])
def reset():
  activities.clear()
  session['gold_amt'] = 0
  session['moves'] = 0
  return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
