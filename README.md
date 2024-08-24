markdown
Copy code
# Car Price Predictor Pakistan

This is a web application that predicts the price of used cars based on various features such as make, model, year, mileage, fuel type, engine capacity, transmission, and location. The application uses a machine learning model trained on a dataset of used car prices in Pakistan.
![image](https://github.com/user-attachments/assets/01492ddc-7c21-447b-b3d4-1ce23881068f)
![image](https://github.com/user-attachments/assets/43299fff-bc5c-4894-a9a7-f3b57ecfd1b4)



## Features

- Predict the price of a car by entering its details.
- View a list of vehicles and their details.
- Built with React for the frontend and Flask for the backend.
- Tailwind CSS is used for styling the frontend.

## Project Structure

```bash
CarPricePredictor/
├── server/                     # Flask backend
│   ├── app.py                  # Main Flask application
│   ├── models.py               # SQLAlchemy models
│   ├── MachineLearning/        # Directory containing the ML model
│   │   ├── car_price_model.pkl # Trained ML model
│   │   ├── modelTraining.py    # Script to train the ML model
│   ├── data/                   # Directory containing the database
│   │   └── vehicles.db         # SQLite database file
│   ├── load_cleaned_data.py    # Script to load cleaned data into the database
│   └── requirements.txt        # Python dependencies
├── client/                     # React frontend
│   ├── src/
│   │   ├── components/         # React components
│   │   │   ├── PredictForm.jsx # Form component for predicting car prices
│   │   │   ├── Navbar.jsx      # Navbar component
│   │   ├── services/           # API service files
│   │   │   └── api.js          # Axios API service
│   │   ├── App.js              # Main App component
│   │   ├── index.js            # React entry point
│   ├── public/
│   │   └── index.html          # Main HTML file
│   ├── tailwind.config.js      # Tailwind CSS configuration
│   └── package.json            # NPM dependencies
└── README.md                   # Project documentation
```
## Prerequisites
Python 3.x (for the backend)
Node.js (for the frontend)
pipenv or virtualenv (recommended for managing Python packages)
Setup Instructions
Backend (Flask)

Clone the repository:

bash
Copy code
```
git clone https://github.com/yourusername/CarPricePredictor.git
cd CarPricePredictor/server
```
Set up a virtual environment:

Using pipenv:

bash
```
pipenv install
pipenv shell
```
Or using virtualenv:

bash
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```
Load the cleaned data into the SQLite database:

bash
```
python load_cleaned_data.py
```
Run the Flask server:

bash
```
python app.py
```
The server will start on http://127.0.0.1:5000.

Frontend (React)
Navigate to the client directory:

bash
```
cd ../client
```
Install the dependencies:

bash
```
npm install
```
Run the development server:

bash
```
npm start
```
The frontend will be accessible at http://localhost:3000.

Tailwind CSS Setup
The project uses Tailwind CSS for styling. The configuration is located in client/tailwind.config.js. Ensure that Tailwind is correctly set up in the postcss.config.js and index.css files.

Deploying the Application
To deploy the application:

Build the React app:

bash
```
npm run build
```
Serve the built static files from a production-ready web server like Nginx or serve them with Flask.

API Endpoints
GET /api/vehicles: Retrieve a list of vehicles from the database.
POST /api/predict: Predict the price of a car based on input features.
Training the Machine Learning Model
To retrain the machine learning model:

Modify the modelTraining.py script as needed.

Run the script to train and save the model:

bash
```
python modelTraining.py
```
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## Contact
For any questions or support, please open an issue in this repository.

Thank you for using the Car Price Predictor!
