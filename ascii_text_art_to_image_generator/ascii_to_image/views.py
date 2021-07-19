from django.shortcuts import render
from django.http import HttpResponse
from .convert import convert_ascii_to_image


def index(request):
    converted = False
    text = ''
    hashed_txt = "nope"
    if 'ascii-art-text' in request.POST:
        text = request.POST['ascii-art-text']
        hashed_txt = hash(text)
        for i in range(3):
            im = convert_ascii_to_image(text, i)
            im.save('ascii_to_image/static/ascii_to_image/output-' + str(hashed_txt) + '-' + str(i) + '.png')
        converted = True
    context = {
        "text": text,
        "hashed_txt": hashed_txt,
        "converted": converted
    }
    return render(request, 'ascii_to_image/index.html', context)
