from dadata import Dadata

from django.shortcuts import render


def index(request):
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    token = "a9de885f2cd384d67b27cfbfcd3597555808ccf0"
    dadata = Dadata(token)
    result = dadata.iplocate("217.175.5.185")
    context = {
        'api': result['data']['city_with_type'],
        'ip': get_client_ip(request)
    }
    return render(request, 'recipe/index.html', context)
