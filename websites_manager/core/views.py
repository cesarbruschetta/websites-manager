
from django.shortcuts import render
from django.conf import settings

from os import scandir, path
import magic


# Create your views here.
def file_serve(request, path_name):
    template_name = "file_server.html"

    local_path = path.join(settings.ROOT_FILE_PATH, path_name)

    # import pdb; pdb.set_trace()

    imagens = []
    videos = []
    others = []
    directories = []
    for entry in scandir(local_path):
        if entry.is_file():
            file_path = entry.path.replace(settings.ROOT_FILE_PATH, settings.STATIC_URL)
            mine_type = magic.from_file(entry.path, mime=True)
            if "image" in mine_type:
                imagens.append({
                    "name": entry.name,
                    "path": file_path,
                })
            elif "video" in mine_type:
                videos.append({
                    "name": entry.name,
                    "path": file_path,
                })
            else:
                others.append({
                    "name": entry.name,
                    "path": file_path,
                })

        if entry.is_dir():
            directories.append({
                "name": entry.name,
                "path": entry.path.replace(settings.ROOT_FILE_PATH, "")
            })

    context = {
        "path_name": path_name,
        "directories": directories,
        "imagens": imagens,
        "videos": videos,
        "others": others,
    }

    return render(request, template_name, context)
