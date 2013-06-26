__author__ = 'waiter'

from django.core.urlresolvers import reverse
from rest_framework_framework



from djangorestframework.resources import ModelResource
from models import *

class ProductItemResource(ModelResource):
    model = Product
    fields = ('name', )


