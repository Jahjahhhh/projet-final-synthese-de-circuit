from django.shortcuts import render
from .test_uart import send_uart

def index(request):
    """View function for home page of site."""
    # Render the HTML template index.htmll with the data in the context variable
    context = {}
    return render(request, 'index.html', context=context)

def bouton1(request):
    status = "'A'"
    print('[ACTION]' + status)
    print('[UART]' + send_uart("/dev/ttyACM0", 'A'))

    context = {'Message':status}
    return render(request, 'index.html', context=context)

def bouton2(request):
    status = "'B'"
    print('[ACTION]' + status)
    print('[UART]' + send_uart("/dev/ttyACM0", 'B'))
    context = {'Message':status}
    return render(request, 'index.html', context=context)

def bouton3(request):
    status = "'C'"
    print('[ACTION]' + status)
    print('[UART]' + send_uart("/dev/ttyACM0", 'C'))
    context = {'Message':status}
    return render(request, 'index.html', context=context)

def bouton4(request):
    status = "'D'"
    print('[ACTION]' + status)
    print('[UART]' + send_uart("/dev/ttyACM0", 'D'))
    context = {'Message':status}
    return render(request, 'index.html', context=context)
