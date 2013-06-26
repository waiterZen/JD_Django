#code=utf-8
# Create your views here.

from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

# app specific files

from models import *
from forms import *


def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    t = get_template('ExDataApp/create_product.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_product(request):
  
    list_items = Product.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('ExDataApp/list_product.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_product(request, id):
    product_instance = Product.objects.get(id = id)

    t=get_template('ExDataApp/view_product.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_product(request, id):

    product_instance = Product.objects.get(id=id)

    form = ProductForm(request.POST or None, instance = product_instance)

    if form.is_valid():
        form.save()

    t=get_template('ExDataApp/edit_product.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))


def  search_product(request):

    list_items2 =[]

    try:
        id  = int(request.GET.get('id', '0'))
        if(id != 0):
             product_instance = Product.objects.get(id = id)
             list_items2.append(product_instance)

    except Exception,err:
        print err

    try:
        import urllib
        query = request.GET.get('query').encode('utf8')
        #query =urllib.unquote(request.GET.get('query')).decode('utf8')

        # sql =' select * from   ExDataAPP_product where  errorType like "%' + query + '%";'
        # print sql
        # list_items2 = Product.objects.raw(sql)

        list_items2 = Product.objects.filter(errorType__contains = query)

        from django.db import connection
        print connection.queries
    except Exception ,err :
            print err

    t=get_template('ExDataApp/search_product.html')
    c=RequestContext(request,locals())

    response = HttpResponse(t.render(c))


    return response

def process_response(self, request, response):
            t = 0
            for x in connection.queries:
                if float(x['time']): print x
                t+=float(x['time'])
            print 'time count:',t,'=' * 40
            return response