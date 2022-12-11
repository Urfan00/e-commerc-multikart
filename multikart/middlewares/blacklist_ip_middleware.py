from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render



class BlackListIPMiddleware(MiddlewareMixin):
    BLACK_LIST_IP = [
        ''
    ]

    def process_request(self, request):
        if request.META.get('REMOTE_ADDR') in self.BLACK_LIST_IP:
            return render(request, '404.html')
