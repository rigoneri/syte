# Modified from http://djangosnippets.org/snippets/243/
import base64

from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.conf import settings

#############################################################################
#
def view_or_basicauth(view, request, realm = "", *args, **kwargs):
    if 'HTTP_AUTHORIZATION' in request.META:
        auth = request.META['HTTP_AUTHORIZATION'].split()
        if len(auth) == 2:
            # NOTE: We are only support basic authentication for now.
            #
            if auth[0].lower() == "basic":
                uname, passwd = base64.b64decode(auth[1]).split(':')
                if uname == settings.BUILTIN_POST_USERNAME and passwd == settings.BUILTIN_POST_PASSWORD:
                    return view(request, *args, **kwargs)

    response = HttpResponse()
    response.status_code = 401
    response['WWW-Authenticate'] = 'Basic realm="%s"' % realm
    return response

#############################################################################
#
def logged_in_or_basicauth(realm = ""):
    """
    A simple decorator that requires a user to be logged in. If they are not
    logged in the request is examined for a 'authorization' header.

    If the header is present it is tested for basic authentication and
    the user is logged in with the provided credentials.

    If the header is not present a http 401 is sent back to the
    requestor to provide credentials.

    The purpose of this is that in several django projects I have needed
    several specific views that need to support basic authentication, yet the
    web site as a whole used django's provided authentication.

    The uses for this are for urls that are access programmatically such as
    by rss feed readers, yet the view requires a user to be logged in. Many rss
    readers support supplying the authentication credentials via http basic
    auth (and they do NOT support a redirect to a form where they post a
    username/password.)

    Use is simple:

    @logged_in_or_basicauth
    def your_view:
        ...

    You can provide the name of the realm to ask for authentication within.
    """
    def view_decorator(func):
        def wrapper(request, *args, **kwargs):
            return view_or_basicauth(func, request,
                realm, *args, **kwargs)
        return wrapper
    return view_decorator