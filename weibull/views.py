from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import WeibullForm


def home(request):
    context = {}
    if request.method == 'POST':
        form = WeibullForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            alpha = data['alpha']
            beta = data['beta']
            increment = data['increment']
            initial = data['initial']
            repetitions = data['repetitions']
            values = weibull(alpha, beta, increment, initial, repetitions)
            context['data'] = values
    else:
        form = WeibullForm()
    context['form'] = form
    return render_to_response('home.html', context, RequestContext(request))


def weibull(alpha, beta, increment=0.05, initial=0, repetitions=100):
    import math
    data = []
    i = 0
    x = initial
    while i < repetitions:
        r = -1 * math.pow(x / beta, alpha)
        result = 1 - math.pow(math.e, r)
        data.append({
            'x': x,
            'y': result
        })
        x += increment
        i += 1
    return data
