from django.shortcuts import render
from .convert import convert_ascii_to_image
from django.conf import settings
from django.core.files.storage import default_storage


def index(request):
    converted = False
    text = ''
    hashed_txt = "nope"
    paths = []
    error = ''
    if 'ascii-art-text' in request.POST:
        text = request.POST['ascii-art-text']
        if text == '':
            error = "ASCII text art cannot be empty."
        else:
            num_rows = len(text.split('\n'))
            num_cols = max([len(row) for row in text.split('\n')])
            if num_rows > 200:
                error = "Too many rows (max 200)"
            elif num_cols > 300:
                error = "Too many columns (max 300)"
        if error == '':
            hashed_txt = hash(text)
            for i in range(3):
                image = convert_ascii_to_image(text, i)
                filename = 'generated-images/' + str(hashed_txt) + '-' + str(i) + '.png'
                path = default_storage.save(filename, image)
                paths.append(settings.MEDIA_URL + path)
            converted = True
    context = {
        "error": error,
        "paths": paths,
        "text": text,
        "converted": converted
    }
    return render(request, 'ascii_to_image/index.html', context)
