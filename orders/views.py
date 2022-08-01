# Create your views here.

from django.core import serializers
from django.http import HttpResponse

from orders.models import Order



def index(request):
    qs = Order.objects.filter(from_seller=5).all()
    qs_json = serializers.serialize('json', qs)
    return HttpResponse(qs_json, content_type='application/json')


