import http.client, urllib.parse
import geocoder
from .models import *
from django.core.files.base import ContentFile
from django.conf import settings
import os
from shutil import copyfile
import base64
import shutil

class Distancia:
    def get_bodega(bodega1):
        try:
            return Bodega.objects.get(id=bodega1)
        except Bodega.DoesNotExist:
            raise None

    def get_distancia(bodega1,bodega2):
        origen=Distancia.get_bodega(bodega1)
        destino=Distancia.get_bodega(bodega2)
        post=str(origen.direccion +" "+ str(origen.numeracion) +", "+ 
                                        origen.ciudad.nombre +", "+
                                        "Arica y Parinacota"+", "+ 'Chile')
#         print (post)
#         oc = geocoder.osm("Los Castaños 11975, 8010277 El Bosque, Región Metropolitana, Chile")

#         print (oc)
#         print('Calle El Almendro 6, Córdoba, Spain')
#         a=('Calle El Almendro 6, Córdoba, Spain')

#         loc = geocoder.osm(a)

#         print (loc)
#         print (loc.latlng)
# #g.json

        conn = http.client.HTTPConnection('geocode.xyz')

        params = urllib.parse.urlencode({
            'auth': '365877984424120278456x96835',
            'locate': post,
            'region': 'CL',
            'json': 1,
            })

        conn.request('GET', '/?{}'.format(params))

        res = conn.getresponse()
        data = res.read()

        print(data.decode('utf-8'))
