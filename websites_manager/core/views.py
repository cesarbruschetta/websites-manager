
from django.shortcuts import render
from django.conf import settings
from django.utils.encoding import force_bytes

from os import scandir, path
import magic


# Create your views here.

def home(request):
    context = {
        "active": "home"
    }

    return render(request, "home.html", context)


def file_serve(request, path_name):
    template_name = "file_server.html"

    local_path = path.join(settings.FILE_PATH_ROOT, path_name)

    # import pdb; pdb.set_trace()

    imagens = []
    videos = []
    others = []
    directories = []
    for entry in scandir(local_path):
        file_path = force_bytes(entry.path).decode('utf8', 'surrogateescape')

        if entry.is_file():
            file_path = file_path.replace(settings.FILE_PATH_ROOT,
                                          settings.FILE_PATH_URL)
            try:
                mine_type = magic.from_file(entry.path, mime=True)
            except Exception:
                mine_type = ""

            if "image" in mine_type:
                imagens.append({
                    "name": entry.name,
                    "path": file_path,
                })
            elif "video" in mine_type:
                videos.append({
                    "name": entry.name,
                    "path": file_path,
                    "mine_type": mine_type
                })
            else:
                others.append({
                    "name": entry.name,
                    "path": file_path,
                })

        if entry.is_dir():
            directories.append({
                "name": entry.name,
                "path": file_path.replace(settings.FILE_PATH_ROOT, "")
            })

    context = {
        "active": "file_serve",
        "path_name": path_name,
        "path_back": path.dirname(path_name),
        "local_name": path_name.split("/")[-1],
        "directories": directories,
        "directories_length": len(directories),
        "imagens": imagens,
        "imagens_length": len(imagens),
        "videos": videos,
        "videos_length": len(videos),
        "others": others,
        "others_length": len(others),
    }

    return render(request, template_name, context)
