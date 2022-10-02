import logging
import pandas as pd

from fileinput import filename
from flask import Flask,request,render_template

from utils.utils import read_request_data
from model.inference import predict_model

app=Flask(__name__)

def read_csv_file(filename):
     try:
          logging.info(f'Reading CSV File {filename}')
          return pd.read_csv(filename)
     except Exception as err:
          logging.error(f'Failed in loding csv file {filename}')

logging.basicConfig(format=(),level=logging.INFO)


@app.route('/')
def home():
     data = read_csv_file('./cleaned_data.csv')
     
     Item_Fat_Content=sorted(data['Item_Fat_Content'].unique())
     Item_Type=sorted(data['Item_Type'].unique())
     Outlet_Size=sorted(data['Outlet_Size'].unique())
     Outlet_Location_Type=sorted(data['Outlet_Location_Type'].unique())
     Outlet_Type=sorted(data['Outlet_Type'].unique())

     return render_template("index.html", Item_Fat_Content= Item_Fat_Content, Item_Type= Item_Type, Outlet_Size=Outlet_Size,
     Outlet_Location_Type= Outlet_Location_Type, Outlet_Type=Outlet_Type)


@app.route('/predict',methods=['POST'])
def predict():
     """
     This function returns the predicted data back to the webpage. 
     """
     sales_data = read_request_data(request=request)
     prediction = predict_model(sales_data)
     return str(prediction[0])

if __name__=='__main__':
     app.run(debug=True)
