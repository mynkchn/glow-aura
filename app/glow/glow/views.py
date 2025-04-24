from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.http import HttpResponse

def send_lawtech_design(request):
    subject = "Glow Aura - LawTech Assignment Email Design"
    from_email = 'mynkchn.pu@gmail.com'
    to_email = ['legaltech.testdesk@gmail.com']  # replace with the actual address

    html_content = render_to_string('index.html')  # this is your designed email

    msg = EmailMultiAlternatives(subject, '', from_email, to_email)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    return HttpResponse("Styled email sent to LawTech!")
