from django.shortcuts import render
from .convert import convert_ascii_to_image
from django.conf import settings
from django.core.files.storage import default_storage


def index(request):
    converted = False
    text = ''
    hashed_txt = "nope"
    paths = []
    if 'ascii-art-text' in request.POST:
        text = request.POST['ascii-art-text']
        hashed_txt = hash(text)
        for i in range(3):
            image = convert_ascii_to_image(text, i)
            filename = 'generated-images/' + str(hashed_txt) + '-' + str(i) + '.png'
            path = default_storage.save(filename, image)
            paths.append(settings.MEDIA_URL + path)
        converted = True
    context = {
        "paths": paths,
        "text": text,
        "hashed_txt": hashed_txt,
        "converted": converted
    }
    return render(request, 'ascii_to_image/index.html', context)
