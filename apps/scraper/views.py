from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required

@login_required
def scraper_form(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        keyword = request.POST.get('keyword')  # palabra clave opcional

        try:
            response = requests.get(url)
            response.raise_for_status()
        except Exception as e:
            return render(request, 'scraper/form.html', {'error': f"Error al acceder a la URL: {e}"})

        soup = BeautifulSoup(response.text, 'html.parser')

        # Obtener todos los títulos h2
        if keyword:
            titulos = [
                h2.get_text() for h2 in soup.find_all('h2')
                if keyword.lower() in h2.get_text().lower()
            ]
        else:
            titulos = [h2.get_text() for h2 in soup.find_all('h2')]

        # Guardar resultados en sesión para enviarlos luego
        request.session['scraper_resultados'] = titulos
        request.session['scraper_url'] = url

        return render(request, 'scraper/resultados.html', {
            'titulos': titulos,
            'url': url,
            'keyword': keyword
        })
    return render(request, 'scraper/form.html')


@login_required
def scraper_enviar(request):
    titulos = request.session.get('scraper_resultados', [])
    url = request.session.get('scraper_url', '')

    if titulos:
        cuerpo = f"Resultados del scraping en {url}:\n\n" + "\n".join(titulos)
        send_mail(
            'Resultados del Scraper',
            cuerpo,
            settings.EMAIL_HOST_USER,
            [request.user.email],
            fail_silently=False,
        )
        mensaje = "Resultados enviados por correo."
    else:
        mensaje = "No hay resultados para enviar."

    return render(request, 'scraper/resultados.html', {
        'titulos': titulos,
        'url': url,
        'mensaje': mensaje
    })
