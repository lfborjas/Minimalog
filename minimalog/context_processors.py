'''
Created on 28/07/2010

@author: lfborjas
'''
def blog(request):
    from django.conf import settings
    from google.appengine.api import users
    user = users.get_current_user()
    login_url = users.create_login_url(request.path) if not user else ""
    logout_url = users.create_logout_url(request.path) if user else ""
    is_admin = users.is_current_user_admin() if user else False
    return {'fb_key': settings.FACEBOOK_API_KEY,
            'user': user,
            'login_url': login_url,
            'logout_url': logout_url,
            'is_admin': is_admin}