from flask import request

def read_request_data(request):

    Item_Weight=float(request.form.get('Item_Weight'))
    Item_Fat_Content = request.form.get('Item_Fat_Content')
    Item_Visibility = request.form.get('Item_Visibility')
    Item_Type = request.form.get('Item_Type')
    Item_MRP = request.form.get('Item_MRP')
    Outlet_Size = request.form.get('Outlet_Size')
    Outlet_Location_Type = request.form.get('Outlet_Location_Type')
    Outlet_Type = request.form.get('Outlet_Type')
    Outlet_Establishment_Year = request.form.get('Outlet_Establishment_Year')

    sales_data = [Item_Weight, Item_Fat_Content, Item_Visibility, Item_Type,Item_MRP, Outlet_Size, Outlet_Location_Type, Outlet_Type, Outlet_Establishment_Year]

    return sales_data