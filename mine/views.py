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


# def results(request, cargo_id):
#     cargo = get_object_or_404(Cargo, pk=cargo_id)
#     return render(request, 'cargo/results.html', {'cargo': cargo})


def calc(request, cargo_id):
    cargo = get_object_or_404(Cargo, pk=cargo_id)

    result_success = []
    result_warning = []
    coordinates = ''

    if request.method == 'POST':
        for store in Store.objects.all():
            delivery = History(store=store, cargo=cargo, coordinates=request.POST.get("coordinates", ""))
            coordinates = delivery.coordinates

            if delivery.enter_to_polygon:
                result_success.append(delivery.calc())
            else:
                result_warning.append(delivery.calc())

    return render(request, 'cargo/index.html', {
        'cargos': [cargo],
        'coordinates': coordinates,
        'result_success': result_success,
        'result_warning': result_warning,
    })

    # return HttpResponseRedirect(reverse('cargo:detail', args=(cargo.id,)))
