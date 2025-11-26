from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from reportlab.pdfgen import canvas
from io import BytesIO
from apps.alumnos.models import Alumno

@login_required
def enviar_pdf(request, id):
    alumno = get_object_or_404(Alumno, id=id, usuario=request.user)

    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 750, f"Alumno: {alumno.nombre}")
    p.drawString(100, 730, f"Carrera: {alumno.carrera}")
    p.drawString(100, 710, f"Promedio: {alumno.promedio}")
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()

    email = EmailMessage(
        "Informe Alumno",
        "Adjunto PDF con datos del alumno.",
        "tuemail@gmail.com",  # remitente
        [request.user.email], # destinatario
    )
    email.attach("informe.pdf", pdf, "application/pdf")
    email.send()

    return redirect("dashboard")
