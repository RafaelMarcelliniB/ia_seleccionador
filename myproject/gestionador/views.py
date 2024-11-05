from django.shortcuts import render

def pagina_principal_view(request):
    return render(request, 'Pagina_principal.html')

def estadisticas_mensuales(request):
    return render(request, 'estadisticas_mensuales.html')

def iniciar_sesion(request):    
    return render(request, 'iniciar_sesion.html')

def selector_ia(request):
    return render(request, 'selector_ia.html')

def selector_ia_log(request):
    return render(request, 'selector_ia_log.html')

def pagina_principal_log(request):
    return render(request, 'pagina_principal_log.html')

def registrar_usuario(request):
    return render(request, 'registro.html')