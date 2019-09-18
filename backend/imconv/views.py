from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .conv import converter

# Create your views here.
@csrf_exempt
def index(request):
    data = {}

    extension = request.POST.get("extension", None)
    img_token = request.POST.get("img_token", None)
    if extension and img_token:
        data["file_id"] = converter(img_token, extension)

    return render(request, "index.html", data)
