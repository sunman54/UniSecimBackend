from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from .models import Uni
from .forms import UniversityForm


def uni_main(request):
    universities = Uni.objects.all()
    return render(request, 'University/index.html', {'universities' : universities})

def uni_index(request):
    return HttpResponse("<h1>Index Page</h1>")


def uni_detail(request, id):
    university =get_object_or_404(Uni, id=id)

    context = {
        'uni' : university,
    }

    return render(request, 'University\details.html', context)


def uni_create(request):
    form = UniversityForm(request.POST or None)
    if form.is_valid():
        university = form.save()
        return HttpResponseRedirect(university.get_absolute_url())
    context = {
        'form' : form
    }
    return render(request, 'University/form.html', context)


def uni_update(request, id):
    university = get_object_or_404(Uni, id=id)
    form = UniversityForm(request.POST or None, instance=university)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(university.get_absolute_url())

    context = {
        'form': form
    }
    return render(request, 'University/form.html', context)


def uni_delete(request,id):
    university = get_object_or_404(Uni, id=id)
    university.delete()
    return redirect('/university/')
