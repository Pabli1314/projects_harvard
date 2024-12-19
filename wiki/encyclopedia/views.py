from django.shortcuts import render
from . import util
from .util import get_entry
from .convert import convertHTML
from django.utils.safestring import mark_safe
from django.shortcuts import redirect

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def results(request, title):
    entry = get_entry(title)
    if entry is None:
    
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries(),
            "message": True # We set the “message” key to true so that it displays a legend that the user search was not found.
        })
    #
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "results": mark_safe(convertHTML(entry)),
        })
  


def searchEncyclopedia(request):
    if request.method == "GET":
        q = request.GET.get('q', '').strip()  # Obtener la consulta
        entries = util.list_entries()  # Obtener todas las entradas disponibles
        entry = get_entry(q)  # Intentar obtener una entrada exacta

        # Si se encuentra una coincidencia exacta, redirigir a la página de esa entrada
        if entry:
            return render(request, "encyclopedia/index.html", {
                "results": mark_safe(convertHTML(entry)),  # Mostrar la entrada exacta
                "entries": entries,  # Lista todas las entradas (opcional)
            })

        # Buscar coincidencias parciales (subcadenas)
        matches = [e for e in entries if q.lower() in e.lower()]

        # Si hay coincidencias parciales, mostrar la página de resultados de búsqueda
        if matches:
            return render(request, "encyclopedia/index.html", {
                "matches": matches,  # Mostrar las coincidencias parciales
                "query": q
            })

        # Si no hay coincidencias, mostrar un mensaje de error
        return render(request, "encyclopedia/index.html", {
            "message": "No se encontraron resultados para la búsqueda.",
            "entries": entries  
        })

