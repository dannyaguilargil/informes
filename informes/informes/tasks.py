from celery import shared_task
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings


@shared_task
def enviar_alarma(correo, mensaje):
    send_mail(
        'Alarma del informe {informe.nombre}',
        mensaje,
        settings.DEFAULT_FROM_EMAIL,
        [correo],
        fail_silently=False,  
    )

@shared_task
def enviar_alarma2(correo, mensaje_html, nombre_informe):
    subject = f'Alarma del informe: {nombre_informe}'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = [correo]
    text_content = "Alarma del Sistema de Informes"

    email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    email.attach_alternative(mensaje_html, "text/html")
    
    # Enviar el correo
    email.send()


@shared_task(bind=True) 
def prueba():
    print('Celery esta funcionando!')