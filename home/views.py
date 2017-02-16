import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader


def home(request):
    return render(request, 'index.html', [])


def error400(request):
    return __error(request, 400)


def error403(request):
    return __error(request, 403)


def error404(request):
    return __error(request, 404)


def error500(request):
    return __error(request, 500)


def __error(request, status):
    template = loader.get_template('error.html')
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META.get('HTTP_X_FORWARDED_FOR')
    elif request.META.get('HTTP_X_REAL_IP'):
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        ip = request.META.get('REMOTE_ADDR')
    context = Context({
        'status': status,
        'ip': ip,
        'path': request.get_full_path(),
        'date': datetime.datetime.now().strftime("%Y-%m-%d"),
        'time': datetime.datetime.now().strftime("%H:%M:%S (%s)"),
        'browser': '%s' % request.META['HTTP_USER_AGENT'],
    })
    return HttpResponse(content=template.render(context), content_type='text/html; charset=utf-8', status=status)
