from django.shortcuts import (
render
)
from django.template import RequestContext

# HTTP Error 404
def not_found(request, exception): #HttpResponseNotFound):
    response = render(
        request,
        '404.html',
        #context_instance=RequestContext(request)
        )

    response.status_code = 404

    return response

# HTTP Error 500
def server_error(request):
    response = render(
        request,
        '500.html',
        #context_instance=RequestContext(request)
        )

    response.status_code = 500

    return response

def bad_request(request, exception): #HttpResponseNotFound):
    response = render(
        request,
        '403.html',
        #context_instance=RequestContext(request)
        )

    response.status_code = 403

    return response
