from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from produits.models import Produit
from .forms import ProduitForm, PureProduitForm
from django.contrib import messages

def product_detail_views(request):
    obj = Produit.objects.all()
    context = {
        "objects" : obj
    }
    return render(request, 'product/detail.html', context)

#def product_create_view(request):
    #form = ProduitForm(request.POST or None)
    #message = ''
#    if request.method == 'POST':
#        form = ProduitForm(request.POST)
#        if form.is_valid():
#            form.save()
#            messages.success(request, "article a bien été enregistré")
#            return redirect('product_create')
#    else:
#        form = ProduitForm()
#    return render(request, 'product/create.html', {'form':form})

#def product_create_view(request):
#    message = ''
#    if request.method == 'POST':
#        data = request.POST
#        nom = data.get('nom')
#        description = data.get('description')
#        prix = data.get('prix')
#
#        Produit.objects.create(nom=nom, description=description, prix=prix)
#        message = 'produit créé avec success'
#    return render(request, 'product/create.html', {'message':message})

def product_create_view(request, *args, **kwargs):
    message = ''
    data_initial = {
        'nom' : 'produit',
        'description':'description du produit',
        'prix': 20
    }
    form = PureProduitForm(request.POST or None, initial=data_initial)
    if form.is_valid():
        data = form.cleaned_data
        Produit.objects.create(**data)
        message = 'formulaire envoyer avec success'
        form = PureProduitForm()
    return render(request, 'product/create.html', {'message': message, 'form':form})

def home_view(request, *args, **kwargs):
    list = [3,4,5,7,8,8]
    user = request.user
    context = {
        "list":list,
        "user" : user
    }
    return render(request, "home.html", context)

def about_view(request, *args, **kwargs):
    list_number = [1, 3, 6, 9, 9, 0]
    context = {
        'list_number': list_number,
        'title':'about us',
        'my_number':123,
        'html': '<h1> hello world</h1>',
        'html1': '<center> hello world</center>'
        }
    return render(request, "about.html", context)

def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Contact page </h1>")
    return render(request, "contact.html")

def product_detail_view(request, my_id):
    obj =get_object_or_404(Produit, id=my_id)
    return render(request, 'product/detail.html', {'obj':obj})

def product_delete_view(request, my_id):
    obj = get_object_or_404(Produit, id=my_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('product_list')
    return render(request, 'product/delete.html', {'obj':obj})

def product_list_view(request):
    queryset = Produit.objects.all()
    return render(request, 'product/list.html', {'object_list':queryset})