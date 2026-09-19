from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .models import Perro
from .forms import PerroForm

def perro_list(request):
    perros = Perro.objects.all().order_by("id")
    paginator = Paginator(perros, 12)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(request, "perros/perro_list.html", {"page_obj": page_obj})

def perro_detail(request, id):
    perro = get_object_or_404(Perro, id = id)
    return render(request, "perros/perro_detail.html", {"perro": perro})

def perro_create(request):
    if request.method == "POST":
        form = PerroForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "perros/perro_detail.html", {"perro": form.instance})
    else:
        form = PerroForm()
    return render(request, "perros/perro_form.html", {"form": form})

def perro_update(request, id):
    perro = get_object_or_404(Perro, id = id)
    if request.method == "POST":
        form = PerroForm(request.POST, instance = perro)
        if form.is_valid():
            form.save()
            return render(request, "perros/perro_detail.html", {"perro": form.instance})
    else:
        form = PerroForm(instance = perro)
    return render(request, "perros/perro_form.html", {"form": form})

def perro_delete(request, id):
    perro = get_object_or_404(Perro, id = id)
    perro.delete()
    return redirect("perro_list")
