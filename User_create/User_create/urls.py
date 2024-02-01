from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *
####################################################################

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
    path('register/', UserCreate.as_view(), name='register'),
    path('user_activate/<str:uidb64>/<str:token>/',UserActivate.as_view(), name='user_activate'),
    path('', IndexView.as_view(), name='home'),
    path('success_register/', SuccessRegister.as_view(), name='success_register'),

    path('client_register/', ClientRegister.as_view(), name='client_register'),
    path('client_list/', ClientList.as_view(), name='client_list'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
