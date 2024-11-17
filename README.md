# Airbnb-Rent-Prediction


This Flask-based web application predicts the rental price for an Airbnb property based on user-provided details such as neighborhood, distance, and property specifications. It utilizes a pre-trained machine learning model to deliver quick and reliable predictions.

# Features
Neighborhood Selection: Input either a neighborhood name or its corresponding number.
Dynamic Forms: Step-by-step form submission for user-friendly data input.
Prediction Results: Displays a clear and styled prediction of the rental price.
Responsive Design: Works well on different devices, with a clean and intuitive user interface.
Neighborhood List: Displays available neighborhoods for easy reference.


# Technologies Used
Backend: Flask
Frontend: HTML, CSS
Model: Scikit-learn (airbnb.pkl for predictions, scaling.pkl for data normalization)
Hosting: Compatible with Heroku or Docker deployment.


# Setup Instructions
Prerequisites
Python 3.7 or later
Flask (pip install flask)
Pickle files (airbnb.pkl and scaling.pkl)
requirements.txt file for dependencies


Steps to Run Locally
Clone this repository:
git clone <repository_url>
cd <repository_directory>

Install required dependencies:
pip install -r requirements.txt
Place the following files in the root directory:

airbnb.pkl: The pre-trained model.
scaling.pkl: Scaler for normalizing input data.

Start the Flask application:
python app.py

Open your browser and navigate to:
http://127.0.0.1:5000/


# How to Use
Enter your name on the first page.
Choose or enter the neighborhood (name or number).
Provide details about:
Distance to the neighborhood (in kilometers)
Reviews, satisfaction score, accommodations, bedrooms, etc.
Indicate property type:
Private Room: Enter 1 if yes, else 0.
Shared Room: Enter 1 if yes, else 0.
For an entire apartment, enter 0 for both options.
Get the predicted rental price.


# Project Structure
📁 project-directory/
├── 📂 static/
│   └── 📂 image/
│       └── background.png
├── 📂 templates/
│   ├── details.html
│   └── output.html
├── app.py
├── airbnb.pkl
├── scaling.pkl
├── requirements.txt
├── README.md


# Future Improvements
Add user authentication for personalized sessions.
Support for additional input options like amenities or property types.
Mobile-optimized design enhancements.
Deployment to additional platforms like AWS or Azure.
  

# Contributors
Aayan