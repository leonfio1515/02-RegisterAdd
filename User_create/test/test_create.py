from django.urls import reverse
from django.test import RequestFactory
from DB.models import Client
from DB.models import Users
from User_create.views import ClientRegister

import pytest
#-------------------------------------------------------------------#


@pytest.mark.django_db
def test_client():
    view = ClientRegister.as_view()

    client_data = {
        'name':'Leonardo Fiorentino',
        'dni':1234567,
        'gender':'male',
    }

    user_data = {
        'username':'leonfio',
        'first_name':'Leonardo',
        'last_name':'Fiorentino',
        'email':'leonfio1515@gmail.com',
        'password':'Cybe1234',
    }

    Client.objects.create(**client_data)
    Users.objects.create_user(**user_data)

    factory = RequestFactory()
    request = factory.post(reverse('client_register'), data= client_data)
    request.user = Users.objects.get(username = 'leonfio')

    response = view(request)

    assert response.status_code == 302
    assert Client.objects.filter(dni = 1234567).exists()