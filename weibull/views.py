from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    context = {
        'data': weibull(2, 1, initial=2, repetition=51)
    }
    return render_to_response('home.html', context, RequestContext(request))


def weibull(alpha, beta, increment=0.05, initial=0, repetition=100):
    import math
    data = []
    i = 0
    x = initial
    while i < repetition:
        r = -1 * math.pow(x / beta, alpha)
        result = 1 - math.pow(math.e, r)
        data.append({
            'x': x,
            'y': result
        })
        x += increment
        i += 1
    return data
