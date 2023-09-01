from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


router=DefaultRouter()

router.register('blog',views.Blog,basename='blog')     # this is authenticated api and only registered user can CRUD blogs from this website
router.register('getall',views.GetAll,basename='allblogs') # with the help of this url anyone can access all the blogs

urlpatterns = [
    path('',include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
    
]


#     http://127.0.0.1:8000/dj-rest-auth/registration/      for registering
#     http://127.0.0.1:8000/dj-rest-auth/login/             for login into account and as soon as logging in we get access token and refresh token in response
#     http://127.0.0.1:8000/dj-rest-auth/logout/            for logout
#     http://127.0.0.1:8000/api/token/refresh/              for refreshing token and get access token with the help of refresh token



# for registering
# {
#     "username": "",
#     "email": "",
#     "password1": "",
#     "password2": ""
# }


# for loggin in
# {
#     "username": "",
#     "password": ""
# }


#for refreshing token
# {
#     "refresh": ""
# }