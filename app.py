import logging

from flask import Flask, request, render_template

from utils.utils import read_request_data, read_csv_file
from model.inference import predict_model

app = Flask(__name__)
logging.basicConfig(format='%(asctime)s-%(levelname)s- %(message)s ', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)


@app.route('/')
def home():
    """
    #TODO: Explain what this function does
    """
    sales_data = read_csv_file('cleaned_data.csv')
    logging.debug(f'CSV Data Loaded {sales_data}')

    Item_Fat_Content = sorted(sales_data['Item_Fat_Content'].unique())
    Item_Type = sorted(sales_data['Item_Type'].unique())
    Outlet_Size = sorted(sales_data['Outlet_Size'].unique())
    Outlet_Location_Type = sorted(sales_data['Outlet_Location_Type'].unique())
    Outlet_Type = sorted(sales_data['Outlet_Type'].unique())

    return render_template("index.html", Item_Fat_Content=Item_Fat_Content, Item_Type=Item_Type,
                           Outlet_Size=Outlet_Size,
                           Outlet_Location_Type=Outlet_Location_Type, Outlet_Type=Outlet_Type)


@app.route('/predict', methods=['POST'])
def predict():
    """
    This function returns the predicted data back to the webpage.
    """
    sales_data = read_request_data(request=request)
    prediction = predict_model(sales_data)
    logging.info(f'Predictions Made By Model {prediction}')

    return str(prediction[0])


if __name__ == '__main__':
    app.run(debug=False)
