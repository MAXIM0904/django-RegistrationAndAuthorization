from django.core.exceptions import PermissionDenied
from time import strftime

class FilterIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, reguest):
        ip = reguest.META.get("REMOTE_ADDR")
        http_metod = reguest.META.get("REQUEST_METHOD")
        url_address = reguest.META.get("HTTP_HOST")

        text = f"{strftime('%c')}, {http_metod}, {url_address}, {ip}\n"

        with open("logging.txt", "w") as file:
            file.write(text)

        response = self.get_response(reguest)

        return response