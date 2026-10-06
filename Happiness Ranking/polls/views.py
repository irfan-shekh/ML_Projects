from django.shortcuts import render, redirect
import pandas as pd
import pickle
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def first(request):
    if request.method == 'POST' and request.POST.get('pred_button'):
        # Check if this is an AJAX request
        is_ajax = (
            request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' or
            request.POST.get('ajax') == '1'
        )
        
        name = request.POST['Country Name']
        region = request.POST['Region']
        HapScore = request.POST['hapScore']
        standerror = request.POST['se']
        economy = request.POST['eco']
        family = request.POST['fam']
        lifeExp = request.POST['life']
        freedom = request.POST['free']
        government = request.POST['gov']
        generosity = request.POST['Gen']
        dystopia = request.POST['dys']

        if name != "":
            df = pd.DataFrame(columns=['Happiness Score', 'Standard Error',
                                           'Economy (GDP per Capita)', 'Family',
                                           'Health (Life Expectancy)', 'Freedom', 'Generosity',
                                           'Dystopia Residual'])

            df2 = {'Happiness Score': float(HapScore), 'Standard Error': float(standerror),
                       'Economy (GDP per Capita)': float(economy), 'Family': float(family),
                        'Health (Life Expectancy)': float(lifeExp), 'Freedom': float(freedom),
                       'Generosity': float(generosity), 'Dystopia Residual': float(dystopia)}

            df = pd.concat([df, pd.DataFrame([df2])], ignore_index=True)
            # Loading StandardScaler Model
            sc = pickle.load(open(r'polls/HappinessScaler.pickle', 'rb'))
            temp = sc.fit_transform(df)

            # load the model from disk
            filename = 'polls/HappinessModel.pickle'
            loaded_model = pickle.load(open(filename, 'rb'))
            res = loaded_model.predict(temp)
            res = int(abs(res))
            
            if is_ajax:
                return JsonResponse({'result': res})
            else:
                return render(request, 'index.html', {'result': res})
        else:
            if is_ajax:
                return JsonResponse({'error': 'Country name is required'})
            else:
                return redirect('homepage')
    
    # For GET requests or non-prediction POST requests
    return render(request, 'index.html', {'result': 0})

@csrf_exempt
def predict_ajax(request):
    if request.method == 'POST':
        try:
            name = request.POST['Country Name']
            region = request.POST['Region']
            HapScore = request.POST['hapScore']
            standerror = request.POST['se']
            economy = request.POST['eco']
            family = request.POST['fam']
            lifeExp = request.POST['life']
            freedom = request.POST['free']
            government = request.POST['gov']
            generosity = request.POST['Gen']
            dystopia = request.POST['dys']

            if name != "":
                df = pd.DataFrame(columns=['Happiness Score', 'Standard Error',
                                               'Economy (GDP per Capita)', 'Family',
                                               'Health (Life Expectancy)', 'Freedom', 'Generosity',
                                               'Dystopia Residual'])

                df2 = {'Happiness Score': float(HapScore), 'Standard Error': float(standerror),
                           'Economy (GDP per Capita)': float(economy), 'Family': float(family),
                            'Health (Life Expectancy)': float(lifeExp), 'Freedom': float(freedom),
                           'Generosity': float(generosity), 'Dystopia Residual': float(dystopia)}

                df = pd.concat([df, pd.DataFrame([df2])], ignore_index=True)
                # Loading StandardScaler Model
                sc = pickle.load(open(r'polls/HappinessScaler.pickle', 'rb'))
                temp = sc.fit_transform(df)

                # load the model from disk
                filename = 'polls/HappinessModel.pickle'
                loaded_model = pickle.load(open(filename, 'rb'))
                res = loaded_model.predict(temp)
                res = int(abs(res))
                
                return JsonResponse({'result': res})
            else:
                return JsonResponse({'error': 'Country name is required'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    
    return JsonResponse({'error': 'Invalid request method'})
