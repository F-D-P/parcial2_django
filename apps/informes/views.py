from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas
from io import BytesIO
from apps.alumnos.models import Alumno

@login_required
def enviar_pdf(request, id):
    alumno = get_object_or_404(Alumno, id=id, usuario=request.user)

    # Generar PDF en memoria
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.setFont("Helvetica-Bold", 14)
    p.drawString(100, 820, "Informe del Alumno")
    p.setFont("Helvetica", 12)
    p.drawString(100, 800, f"Nombre: {alumno.nombre}")
    p.drawString(100, 780, f"Apellido: {alumno.apellido}")
    p.drawString(100, 760, f"Curso: {alumno.curso}")
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()

    # Enviar por correo
    email = EmailMessage(
        subject="Informe en PDF",
        body=f"Adjunto el informe del alumno {alumno.nombre} {alumno.apellido}.",
        from_email=settings.EMAIL_HOST_USER,
        to=[request.user.email],
    )
    email.attach("informe.pdf", pdf, "application/pdf")
    email.send()

    # Renderizar template de confirmación
    return render(request, 'informes/informe.html', {
        'alumno': alumno,
        'mensaje': "Informe enviado por correo."
    })
