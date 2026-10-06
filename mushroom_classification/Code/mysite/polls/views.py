from django.shortcuts import render, redirect
import pandas as pd
import pickle
import os

def index_func(request):
    res = 0
    error_message = ""
    
    if request.method == 'POST':
        try:
            capShape = request.POST.get('capShape')
            CapSurface = request.POST.get('CapSurface')
            capColor = request.POST.get('capColor')
            bruises = request.POST.get('bruises')
            odor = request.POST.get('odor')
            gillAttach = request.POST.get('gillAttach')
            gillSpace = request.POST.get('gillSpace')
            gillSize = request.POST.get('gillSize')
            gillColor = request.POST.get('gillColor')
            stalkShape = request.POST.get('stalkShape')
            stalkRoot = request.POST.get('stalkRoot')
            stalkARing = request.POST.get('stalkARing')
            stalkBRing = request.POST.get('stalkBRing')
            stalkCARing = request.POST.get('stalkCARing')
            stalkCBRing = request.POST.get('stalkCBRing')
            veilType = request.POST.get('veilType')
            veilColor = request.POST.get('veilColor')
            ringNumber = request.POST.get('ringNumber')
            ringType = request.POST.get('ringType')
            sporePrintColor = request.POST.get('sporePrintColor')
            pop = request.POST.get('pop')
            hab = request.POST.get('hab')

            if capShape and all([CapSurface, capColor, bruises, odor, gillAttach, gillSpace, 
                               gillSize, gillColor, stalkShape, stalkRoot, stalkARing, stalkBRing,
                               stalkCARing, stalkCBRing, veilType, veilColor, ringNumber, ringType,
                               sporePrintColor, pop, hab]):
                
                df = pd.DataFrame(columns=['cap-shape','cap-surface','cap-color','bruises','odor',
                                           'gill-attachment','gill-spacing','gill-size','gill-color',
                                           'stalk-shape','stalk-root','stalk-surface-above-ring',
                                           'stalk-surface-below-ring','stalk-color-above-ring',
                                           'stalk-color-below-ring','veil-type','veil-color','ring-number',
                                           'ring-type','spore-print-color','population','habitat'])

                df2 = {'cap-shape': int(capShape),'cap-surface': int(CapSurface),'cap-color': int(capColor),
                       'bruises': int(bruises),'odor': int(odor),'gill-attachment': int(gillAttach),
                       'gill-spacing': int(gillSpace),'gill-size': int(gillSize),'gill-color': int(gillColor),
                        'stalk-shape': int(stalkShape),'stalk-root': int(stalkRoot),'stalk-surface-above-ring':
                        int(stalkARing),'stalk-surface-below-ring': int(stalkBRing),'stalk-color-above-ring':
                        int(stalkCARing),'stalk-color-below-ring': int(stalkCBRing),'veil-type': int(veilType),
                       'veil-color': int(veilColor),'ring-number': int(ringNumber),'ring-type': int(ringType),
                       'spore-print-color': int(sporePrintColor),'population': int(pop),'habitat': int(hab)}

                df = pd.concat([df, pd.DataFrame([df2])], ignore_index=True)
                
                # load the model from disk
                model_path = os.path.join(os.path.dirname(__file__), 'MushsPCA.pickle')
                pca = pickle.load(open(model_path, 'rb'))
                data = pca.transform(df)
                
                model_path1 = os.path.join(os.path.dirname(__file__), 'Mushs.pickle')
                loaded_model = pickle.load(open(model_path1, 'rb'))

                res = loaded_model.predict(data)
                print(res) # ['e' 'p'] -> [0, 1] -> (classes: edible=e, poisonous=p)

                if res[0] == 0:
                    res = 'edible'
                else:
                    res = 'poisonous'
            else:
                error_message = "Please select all required fields"
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            print(f"Error in prediction: {e}")
    else:
        pass

    return render(request, "index.html", {'response': res, 'error_message': error_message})
