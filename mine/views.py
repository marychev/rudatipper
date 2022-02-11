from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from mine.models import Mine, Cargo
from tipper.models import Tipper
from store.models import Store, History


def index(request):
    return render(request, 'cargo/index.html', {
        'cargos': Cargo.objects.all(),
        'mines': Mine.objects.all(),
        'tippers': Tipper.objects.all(),
        'stores': Store.objects.all(),
        'histories': History.objects.all()
    })


def detail(request, cargo_id):
    cargo = get_object_or_404(Cargo, pk=cargo_id)
    return render(request, 'cargo/detail.html', {'cargo': cargo})


def results(request, cargo_id):
    cargo = get_object_or_404(Cargo, pk=cargo_id)
    return render(request, 'cargo/results.html', {'cargo': cargo})


def calc(request, cargo_id):
    cargo = get_object_or_404(Cargo, pk=cargo_id)
    print("!!")
    return render(request, 'cargo/index.html', {
        'cargos': [cargo],
        'result_calc_success': [cargo],
        "result_calc_warning": [cargo],
    })
    # else:
    # return HttpResponseRedirect(reverse('cargo:detail', args=(cargo.id,)))