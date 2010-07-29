'''
Created on 28/07/2010

@author: lfborjas
'''
def blog(request):
    from django.conf import settings   
    
    return {'fb_key': settings.FACEBOOK_API_KEY,
            'user': request.user,
            'login_url': '/login/',
            'logout_url': '/logout/',
            'is_admin': request.user.is_staff}