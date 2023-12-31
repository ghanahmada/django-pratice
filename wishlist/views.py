from django.shortcuts import render
from wishlist.models import BarangWishlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_wishlist(request):
    return render(request, "wishlist.html", context)

data_barang_wishlist = BarangWishlist.objects.all()
context = {
    'list_barang':data_barang_wishlist,
    'nama': 'Kak Cinoy'
}

def show_xml(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data_id = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_id), content_type="application/json")
