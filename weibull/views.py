import math

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
            function = data['function']
            context['initial'] = str(initial)
            values = None
            if function == 'DENSITY':
                values, x_max, y_max = weibull(alpha, beta, increment, initial, repetitions, 1)
            elif function == 'LOWER_CUMULATIVE':
                values, x_max, y_max = weibull(alpha, beta, increment, initial, repetitions, 2)
            elif function == 'UPPER_CUMULATIVE':
                values, x_max, y_max = weibull(alpha, beta, increment, initial, repetitions, 3)
            context['data'] = values
            context['x_max'] = x_max
            context['y_max'] = y_max
    else:
        form = WeibullForm()
    context['form'] = form
    return render_to_response('home.html', context, RequestContext(request))


def weibull(alpha, beta, increment=0.05, initial=0, repetitions=100, function=1):
    data = []
    i = 0
    x = initial
    y_max = 0
    while i < repetitions:
        y = calculate(x, alpha, beta, function)
        if y > y_max:
            y_max = y
        data.append({
            'x': str(x),
            'y': str(y)
        })
        x += increment
        i += 1
    return data, str(x), str(y_max)


def calculate(x, alpha, beta, function):
    r = -1 * math.pow(x / beta, alpha)
    r = math.pow(math.e, r)
    if function == 1:  # density
        r1 = alpha / beta
        r2 = math.pow(x / beta, alpha - 1)
        return r1 * r2 * r
    elif function == 2:  # lower cumulative
        return 1 - r
    elif function == 3:  # upper cumulative
        return r
