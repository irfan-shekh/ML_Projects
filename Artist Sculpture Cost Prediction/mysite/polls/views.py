from django.shortcuts import render, redirect
import pandas as pd
import pickle
import os

def index_func(request):
    res = 0
    error_message = ""
    
    if request.method == 'POST':
        try:
            name = request.POST.get('Name', '').strip()
            repute = request.POST.get('repute', '').strip()
            height = request.POST.get('Height', '').strip()
            width = request.POST.get('Width', '').strip()
            weight = request.POST.get('Weight', '').strip()
            material = request.POST.get('material', '').strip()
            basePrice = request.POST.get('basePrice', '').strip()
            basePriceShipping = request.POST.get('basePriceShipping', '').strip()
            international = request.POST.get('international', '0').strip()
            expressShipment = request.POST.get('expressShipment', '0').strip()
            installments = request.POST.get('installments', '0').strip()
            transport = request.POST.get('Transport', '0').strip()
            fragile = request.POST.get('Fragile', '0').strip()
            customer = request.POST.get('cust', '0').strip()
            remote = request.POST.get('remote', '0').strip()
            waiting = request.POST.get('waiting', '').strip()

            if not name:
                error_message = "Please enter the artist name."
            elif not repute or not height or not width or not weight or not basePrice or not basePriceShipping or not waiting:
                error_message = "Please fill in all numeric fields."
            elif not material:
                error_message = "Please select a material."
            else:
                # Validate and convert inputs
                repute_val = float(repute)
                height_val = float(height)
                width_val = float(width)
                weight_val = float(weight)
                material_val = int(material)
                basePrice_val = float(basePrice)
                basePriceShipping_val = float(basePriceShipping)
                international_val = int(international)
                expressShipment_val = int(expressShipment)
                installments_val = int(installments)
                transport_val = int(transport)
                fragile_val = int(fragile)
                customer_val = int(customer)
                remote_val = int(remote)
                waiting_val = float(waiting)

                # Basic validation ranges
                if not (0 <= repute_val <= 1):
                    error_message = "Artist reputation must be between 0 and 1."
                elif height_val <= 0 or width_val <= 0 or weight_val <= 0:
                    error_message = "Height, width, and weight must be positive numbers."
                elif basePrice_val <= 0 or basePriceShipping_val <= 0:
                    error_message = "Base price and shipping price must be positive numbers."
                else:
                    # Create DataFrame for prediction
                    df = pd.DataFrame(columns=['Artist Reputation', 'Height', 'Width',
                                               'Weight', 'Material', 'Price Of Sculpture', 'Base Shipping Price',
                                               'International', 'Express Shipment', 'Installation Included',
                                               'Transport', 'Fragile', 'Customer Information', 'Remote Location',
                                               'Waiting time'])

                    df2 = {'Artist Reputation': repute_val, 'Height': height_val, 'Width': width_val,
                           'Weight': weight_val, 'Material': material_val, 'Price Of Sculpture':
                            basePrice_val, 'Base Shipping Price': basePriceShipping_val, 'International':
                           international_val, 'Express Shipment': expressShipment_val, 'Installation Included':
                           installments_val, 'Transport': transport_val, 'Fragile': fragile_val,
                           'Customer Information': customer_val, 'Remote Location': remote_val, 'Waiting time':
                           waiting_val}

                    df = pd.concat([df, pd.DataFrame([df2])], ignore_index=True)
                    
                    # Load the model from disk
                    model_path = os.path.join(os.path.dirname(__file__), 'Artist.pickle')
                    if os.path.exists(model_path):
                        loaded_model = pickle.load(open(model_path, 'rb'))
                        res = loaded_model.predict(df)[0]
                        res = round(float(res), 2)
                    else:
                        error_message = "Model file not found. Please ensure the ML model is properly loaded."
                        
        except ValueError as e:
            error_message = f"Invalid input format: {str(e)}. Please check your values."
        except Exception as e:
            error_message = f"An error occurred during prediction: {str(e)}"

        if error_message:
            return render(request, "index.html", {'response': res, 'error': error_message})
    
    return render(request, "index.html", {'response': res})