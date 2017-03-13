
from django.shortcuts import render
from django.conf import settings

from os import scandir, path
import magic


# Create your views here.
def file_serve(request, path_name):
    template_name = "file_server.html"
    context = {}

    local_path = path.join(settings.ROOT_FILE_PATH, path_name)

    # import pdb; pdb.set_trace()

    files = []
    directories = []
    for entry in scandir(local_path):
        if entry.is_file():
            files.append({
                "name": entry.name,
                "path": entry.path.replace(settings.ROOT_FILE_PATH, settings.STATIC_URL),
                "type": magic.from_file(entry.path, mime=True)
            })

        if entry.is_dir():
            directories.append({
                "name": entry.name,
                "path": entry.path.replace(settings.ROOT_FILE_PATH, "")
            })

    # print(files)
    print(directories)

    return render(request, template_name, context)
