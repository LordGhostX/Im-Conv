from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .conv import converter

# Create your views here.
@csrf_exempt
def index(request):
    data = {}

    extension = request.POST.get("extension", None)
    orig_ext = request.POST.get("orig_ext", None)
    img_token = request.POST.get("img_token", None)
    if extension and img_token and orig_ext:
        data["file_id"] = converter(img_token, orig_ext, extension)

    return render(request, "index.html", data)
