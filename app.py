from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Define a list to store the reservation data
reservations = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reservation', methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        num_people = int(request.form['num-people'])
        reservation_date = request.form['reservation-date']

        # Add the reservation data to the reservations list
        reservations.append({'num_people': num_people, 'reservation_date': reservation_date})

        # Render the template with the updated reservation data
        return render_template('reservation.html', reservations=reservations)

    return render_template('reservation.html', reservations=reservations)

@app.route('/menu')
def menu():
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(debug=True)
