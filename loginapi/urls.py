from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'hufusers', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # signup
    path('auth/', obtain_auth_token),  # post request to obtain users' auth token

    # login
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="log_out"),
    path('authenticateuser/',views.get_authenticated_user, name = "get_user_name"),
]
#
#     # Facebook login API
#     path('', views.home_page, name='home_page'),  # redirect to html login file
#     path('accounts/', include('allauth.urls')),
#     path('socialloginauth/<email>/', views.get_social_login_auth, name="social_login_auth"),
#     # set auth token from social account, and get
#
# ]
