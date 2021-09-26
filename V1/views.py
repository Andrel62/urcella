from django.shortcuts import render
import requests

def home(request):
    return render(request, 'pages/home.html')

def keywords(request):
    return render(request, 'pages/keywords.html')

def stores(request):
    return render(request, 'pages/stores.html')

def demoProducts(request):
    url = "https://andreldaga.pythonanywhere.com/api/products/"
    response = requests.get(url)
    data = response.json()

    products = data
    product1=dict()
    product2=dict()
    product3=dict()
    product1['name'] = products[0]['name']
    product1['image'] = products[0]['image']
    product1['price'] = products[0]['price']

    product2['name'] = products[1]['name']
    product2['image'] = products[1]['image']
    product2['price'] = products[1]['price']

    product3['name'] = products[2]['name']
    product3['image'] = products[2]['image']
    product3['price'] = products[2]['price']

    context = {

        'name1': product1['name'],
        'image1': product1['image'],
        'price1': product1['price'],
        'name2': product2['name'],
        'image2': product2['image'],
        'price2': product2['price'],
        'name3': product3['name'],
        'image3': product3['image'],
        'price3': product3['price'],
    
    }

    return render(request, 'pages/demo.html', context)

def cartInfo(request):
    return render(request, 'pages/cart.html')
