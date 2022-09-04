from django.shortcuts import render
import json
import urllib.request
# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=b84f163432addc65dec790ab8a2afcc9').read()
        json_data = json.loads(res)
        # https://openweathermap.org/current
        data = {
            'country_code' : str(json_data['sys']['country']),
            'coordinate' : str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            'temp' : str(round(json_data['main']['temp'] - 273)) + ' C',
            'pressure' : str(json_data['main']['pressure']),
            'humidity' : str(json_data['main']['humidity'])
        }
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city' : city, 'data' : data})
