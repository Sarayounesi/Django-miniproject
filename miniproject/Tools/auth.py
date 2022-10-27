from functools import wraps
from urllib import response
from django.http import HttpResponseRedirect
import jwt
from myapp.models import Person
from rest_framework.response import Response

def role_req(Role):
    def is_auth(view_fun):
        @wraps(view_fun)
        def _wrapped_view(request, *args, **kwargs):
            if 'Token' in request.COOKIES:
                token = request.COOKIES['Token']
                dec = jwt.decode(token, key= "fcgvjbhknkcgvhjbkcvhbjnui465hvgcfd",algorithms="HS256")
                if 'username' in dec:
                    username = dec['username']
                    person = Person.objects.filter(username=username).first()
                    if person :
                        if person.role == Role:
                            return view_fun(request, person, *args, **kwargs)
                        else:
                            return Response('NOT LOGIN', status=403)
            return HttpResponseRedirect(redirect_to='/login')
            

        return _wrapped_view
    return is_auth

