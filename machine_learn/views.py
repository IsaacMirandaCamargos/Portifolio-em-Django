import re
from unittest import result
from webbrowser import get
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from sklearn.utils import resample
from .models import Flores


# Create your views here.
@require_http_methods(['GET'])
def machine_learn_home(request):
    return render(request, 'machine_learn/index.html')


def getPredictions(sl, sw, pl, pw):
    # O usuario precisa nos informar 4 coisas,
    # sepal length, sepal width, petal length e
    # petal width
    import pickle
    model = pickle.load(open("./model_iris/modelos/iris_model.sav", "rb"))
    scaler = pickle.load(open("./model_iris/modelos/iris_scaler.sav", "rb"))
    
    y_pred = model.predict(scaler.transform([[sl,sw,pl,pw]]))
    mask = ['setosa', 'versicolor', 'virginica']

    return str(mask[int(y_pred)])

@require_http_methods(['POST'])
def machine_learn_evaluating(request):
    sl = int(request.POST.get('sepal_length'))
    sw = int(request.POST.get('sepal_width'))
    pl = int(request.POST.get('petal_length'))
    pw = int(request.POST.get('petal_width'))
    predict = getPredictions(sl, sw, pl, pw)

    try:
        flor = Flores.objects.create(sl=sl, sw=sw, pl=pl, pw=pw, predict=predict)
        flor.save()
    except:
        return render(request, 'machine_learn/index.html')
