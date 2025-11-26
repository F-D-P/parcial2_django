import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

@login_required
def scraper_view(request):
    resultados = []
    if request.method == "POST":
        url = request.POST.get("url")
        keyword = request.POST.get("keyword")

        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        textos = [h2.get_text() for h2 in soup.find_all("h2")]

        if keyword:
            resultados = [t for t in textos if keyword.lower() in t.lower()]
        else:
            resultados = textos

        send_mail(
            "Resultados Scraper",
            "\n".join(resultados),
            "tuemail@gmail.com",
            [request.user.email],
        )
    return render(request, "scraper/form.html", {"resultados": resultados})
