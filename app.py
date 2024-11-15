from flask import Flask, request, render_template, redirect, url_for, session
import pickle
import numpy as np

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Load the model and scaler
regmodel = pickle.load(open('airbnb.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

neighborhood_mapping = {
    'De Baarsjes / Oud West': 0,
    'De Pijp / Rivierenbuurt': 1,
    'Centrum West': 2,
    'Centrum Oost': 3,
    'Westerpark': 4,
    'Noord-West / Noord-Midden': 5,
    'Oud Oost': 6,
    'Bos en Lommer': 7,
    'Oostelijk Havengebied / Indische Buurt': 8,
    'Watergraafsmeer': 9,
    'Oud Noord': 10,
    'Ijburg / Eiland Zeeburg': 11,
    'Slotervaart': 12,
    'Buitenveldert / Zuidas': 13,
    'Noord West': 14,
    'Noord Oost': 15,
    'Geuzenveld / Slotermeer': 16,
    'Osdorp': 17,
    'De Aker / Nieuw Sloten': 18,
    'Bijlmer Centrum': 19,
    'Bijlmer Oost': 20,
    'Gaasperdam / Driemond': 21,
    'Westpoort': 22
}

@app.route('/', methods=['GET', 'POST'])
def ask_details():
    # Get the step number from the form, default to 1
    step = int(request.form.get('step', 1))
    # Use a dictionary to store the collected data
    data = {}

    message = ""

    # Process form data based on the current step
    if request.method == 'POST':
        if step == 1:
            session['name'] = request.form['name']
            message = f"Hello, {session['name']}! Welcome to Airbnb Rent Prediction "
            step += 1
        elif step == 2:
            message = f"{session['name']}, please enter your preferred neighborhood."
            step += 1
        elif step == 3:
         
            neighborhood_input = request.form.get('neighborhood', '').strip()

    # Check if input is a digit (i.e., neighborhood number)
            if neighborhood_input.isdigit():
                neighborhood_number = int(neighborhood_input)
                if neighborhood_number  not in neighborhood_mapping.values():
                 session['neighborhood'] = neighborhood_number
                 message = f" {session['name']}! neighborhood number not recognized. Please enter a valid neighborhood."
                else:
                 message = f"{session['name']}, Please help with the distance to your neighborhood."
                 step+=1
            else:
        # Check if the input is a neighborhood name
                neighborhood_number = neighborhood_mapping.get(neighborhood_input)
                if neighborhood_number is not None:
                    session['neighborhood'] = neighborhood_number
                    message = f"Thank you, {session['name']}! Please help with the distance to your neighborhood."
                    step +=1
                else:
                   message = f"{session['name']}, neighborhood name not recognized. Please enter a valid neighborhood."
            #   step += 1
        elif step == 4:
            data['distance'] = float(request.form['distance'])
            message = f"{session['name']},Please fill in the details below."
            step += 1
        elif step == 5:
            # Collect remaining details and convert them to float
            data.update({
                'reviews': float(request.form['reviews']),
                'satisfaction': float(request.form['satisfaction']),
                'accommodates': float(request.form['accommodates']),
                'bedrooms': float(request.form['bedrooms']),
                'day': float(request.form['day']),
                'hour': float(request.form['hour']),
                'minute': float(request.form['minute']),
                'private_room': float(request.form['private_room']),
                'shared_room': float(request.form['shared_room'])
            })
            return redirect(url_for('predict', **data))  # Redirect to predict with all form data

    # Message for step 1
    if step == 1:
        message = "Please Enter your name..."

    # Render the template with the current step and message
    return render_template('details.html', step=step, message=message, data=data , neighborhood_mapping = neighborhood_mapping)

@app.route('/predict')
def predict():
    # Get data from the URL parameters
    name = session.get("name")  # Get the name with a default value if not found
    neighborhood = request.args.get('neighborhood', type=str)
    reviews = request.args.get('reviews', type=float)
    satisfaction = request.args.get('satisfaction', type=float)
    accommodates = request.args.get('accommodates', type=float)
    bedrooms = request.args.get('bedrooms', type=float)
    day = request.args.get('day', type=float)
    hour = request.args.get('hour', type=float)
    minute = request.args.get('minute', type=float)
    distance = request.args.get('distance', type=float)
    private_room = request.args.get('private_room', type=float)
    shared_room = request.args.get('shared_room', type=float)

    # Prepare the input for prediction
    data = [
        neighborhood,
        reviews,
        satisfaction,
        accommodates,
        bedrooms,
        day,
        hour,
        minute,
        distance,
        private_room,
        shared_room
    ]

    # Make the prediction
    final_input = scalar.transform(np.array(data).reshape(1, -1))
    output = regmodel.predict(final_input)[0]

    return render_template('output.html', prediction_text=f"{name}, the predicted rent is ${output:.2f}")

if __name__ == '__main__':
    app.run(debug=True)
