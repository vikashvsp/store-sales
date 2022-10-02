import pickle
import logging
import pandas as pd


def read_model(filename):
    error = False
    try:
        file = open(filename, 'rb')
        model = pickle.load(file)
        logging.info('Successfully Loaded Model')
        return model, False
    except Exception as err:
        logging.error(f'Failed to load Model {err}')
        return "", True


def predict_model(sales_data):
    model, error = read_model("./rf_clf.pkl")
    logging.info(f'Sales Data {sales_data}')
    if not error:
        prediction = model.predict(pd.DataFrame([sales_data], columns=['Item_Weight',
                                                                       'Item_Fat_Content', 'Item_Visibility',
                                                                       'Item_Type',
                                                                       'Item_MRP', 'Outlet_Size',
                                                                       'Outlet_Location_Type', 'Outlet_Type',
                                                                       'Outlet_Establishment_Year']))
        logging.info(f'Predictions are {prediction}')
        return prediction
    else:
        logging.error('Error In Making Predictions')
        return "0"
