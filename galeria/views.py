from django.shortcuts import render


def index(request):

    dados = {
        1: {"nome": "Nebulosa de Carina",
            "legenda": "weebtelescope.org / NASA / James Webb"
            },
        2: {"nome": "Galáxia NGC 1979",
            "legenda": "nasa.org / NASA / Hubble"
            },
        3: {"nome": "Galáxia NGC 1979 OUTRO",
            "legenda": "nasa.org / NASA / Hubble 2"
            },
    }

    return render(request, 'galeria/index.html', {"cards": dados})


def imagem(request):
    return render(request, 'galeria/imagem.html')
