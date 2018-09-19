from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return HttpResponse("Hello, {}.".format(username))
