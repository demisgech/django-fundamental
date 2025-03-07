from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q as Query

from store.models import Product

#  A view: request handle in python not in other languages
# takes(input) => return(output)
# request => response
# action

def basic_filtering_and_retrieving():
    # The all() method returns all entries in the database also colled the manager object
    queryset = Product.objects.all() # get all the products from the database
    
    # A scenario where the querset is evaluated
    # When the queryset is iterated over it
    # Whent it accessed by its index i.e queryset[0], queryset[1:9]
    # When it is converted to a list i.e list(queryset)
    
    # Get all products
    # products = Product.objects.all()
    
    # Get single product
    # try:
    #     product = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass
    
    # Alternative for the above code
    product = Product.objects.filter(pk=0).first() # returns None if the object does not exist
    
    # check_if_exists = Product.objects.filter(pk=0).exists() # returns True or False
    
    product = Product.objects.filter(unit_price=100)
    products = Product.objects.filter(unit_price__gt=100) # greater than 100
    products = Product.objects.filter(unit_price__range=(10,1000)) # greater than 100
    products = Product.objects.filter(collection__id=10) # greater than 100
    products = Product.objects.filter(collection__id__range=(10,20)) # greater than 100
    
    products = Product.objects.filter(title__contains="coffee") # case sensitive
    products = Product.objects.filter(title__icontains="coffee") # case insensitive
    products = Product.objects.filter(title__startswith='apple')
    products = Product.objects.filter(title__istartswith='apple')
    products = Product.objects.filter(title__endswith='fruit')
    products = Product.objects.filter(title__iendswith='fruit')
    
    products = Product.objects.filter(last_update__date='2024-02-01')
    products = Product.objects.filter(last_update__date__gt='2024-02-01')
    products = Product.objects.filter(last_update__date__lt='2024-11-11')
    
    # products = Product.objects.filter(desctiption__isnull=True)
    
    return products


def complex_filtering():
    # AND
    products = Product.objects.filter(unit_price__gt=100, inventory__lt=200) # one option
    products = Product.objects.filter(unit_price__gt=100).filter(inventory__lt=200)# the other option
    # products = Product.objects.filter(Query(unit_price__gt=100) & Query(inventory__lt=200))
    # OR
    products = Product.objects.filter(Query(unit_price__gt=100)| Query(inventory__lt=200))
    
    # NOT
    products = Product.objects.filter(~(Query(unit_price=100)|Query(inventory__lt=200)))
    # products = Product.objects.filter(~(Query(unit_price=100)& Query(inventory__lt=200)))
    return products


def say_hello(request):
    products = basic_filtering_and_retrieving()
    products = complex_filtering()
    return render(request, "hello.html",{"name":"Demis","products":list(products)})