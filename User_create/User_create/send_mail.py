from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.conf import settings

##########################################################################

def enviar_correo_activacion(usuario, request):
    current_site = get_current_site(request)
    uid = urlsafe_base64_encode(force_bytes(usuario.id))
    activate_url = reverse('user_activate', kwargs={
        'uidb64': uid, 'token': default_token_generator.make_token(usuario)})
    activation_link = f"http://{current_site.domain}{activate_url}"
    subject = 'Activación de cuenta'
    message = render_to_string('activate_account.html', {
        'usuario': usuario,
        'activation_link': activation_link,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(usuario.id)),
        'token': default_token_generator.make_token(usuario),
    })
    send_mail(subject, message, settings.EMAIL_HOST_USER, [usuario.email])


def send_mail_client(client,usuario):
    subject = 'New register'
    message = render_to_string('client_register_mail.html', {
        'name': client.name,
        'dni': client.dni,
        'gender': client.gender,

    })
    send_mail(subject, message, settings.EMAIL_HOST_USER, [usuario.email])
