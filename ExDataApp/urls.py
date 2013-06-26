
from django.conf.urls.defaults import *
from models import *
from views import *

from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from resources import *

urlpatterns = patterns('',

    (r'product/create/$', create_product),
    (r'product/list/$', list_product ),
    (r'product/edit/(?P<id>[^/]+)/$', edit_product),
    (r'product/view/(?P<id>[^/]+)/$', view_product),
    (r'product/search$', search_product),
    (r'API/product/items', ListOrCreateModelView.as_view(resource=ProductItemResource )),

)
