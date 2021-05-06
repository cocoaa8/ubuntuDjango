from django.views import View
from django.http import HttpResponse, JsonResponse, FileResponse
from . import getimage
from .models import SmartFarmData
import base64
import json
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404

class IndexView(View):
    def get(self, request):
        item = []
        farms = SmartFarmData.objects.filter(pk=1)
        data = json.loads(serialize('json', farms))
        farms2 = SmartFarmData.objects.filter(pk=2)
        data2 = json.loads(serialize('json', farms2))
        item.append(data)
        item.append(data2)
        return JsonResponse(item, safe = False)


    def post(self, request):
        a = "idsetting"
        b = 2021041717
        c = 2021041718
        d = 2021041719
        e = 2021041720

        NUMBER_OF_ELEMENTS = 5
        gbase64 = []
        gimagecode = []
        go = []
        for i in range(NUMBER_OF_ELEMENTS):
            with open('images/smartfarm{0}.jpeg'.format(i),'rb') as image_file:
                gbase64.append(base64.b64encode(image_file.read()))
            gimagecode.append(i)
        for i in range(NUMBER_OF_ELEMENTS):
            go.append(getimage.image(gbase64[i], gimagecode[i]))
        
        with open('images/smartfarm1.jpeg','rb') as image_file:
                e1 = base64.b64encode(image_file.read())
        
        e1 = str(e1)
        
        SmartFarmData(dataNum = 2,
                      outTemp = 21.1,
                      inTemp = 28.5,
                      outHumidity = 23.1,
                      inHumidity = 25.1,
                      co2ppm = 42.1,
                      src = e1).save()
        
        dataNum = 1,
        datetime = '20210502'
        outTemp = 23.1
        inTemp = 27.5
        outHumidity = 22.1
        inHumidity = 26.1
        co2ppm = 44.1
        src = e1
        
        
        
        
        return JsonResponse(
        {
        'dataNum' : dataNum,
        'datetime' : datetime,
        'outTemp' : outTemp,
        'inTemp' : inTemp,
        'outHumidity' : outHumidity,
        'inHumidity' : inHumidity,
        'co2ppm' : co2ppm,
        'src' : [src]
        }, safe = False)
    
    def put(self, request):
        return HttpResponse("put")
    
    def delete(self, request):
        return HttpResponse("delete")