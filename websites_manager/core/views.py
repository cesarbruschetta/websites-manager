
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.encoding import force_bytes
from django.http import Http404
from .models import FilePathModel, LinksModel

from os import scandir, path
import magic


def home(request):
    context = {
        "active": "home"
    }

    return render(request, "home.html", context)


def redirect_link(request, path_slug):

    obj_link = get_object_or_404(LinksModel, slug=path_slug)
    return redirect(obj_link.link_url)


def file_serve(request, path_slug, path_name):
    template_name = "file_server.html"

    obj_path = get_object_or_404(FilePathModel, slug=path_slug)

    local_path = path.join(obj_path.path_root, path_name)
    try:
        scandir_obj = scandir(local_path)
    except Exception as ex:
        raise Http404(str(ex))

    imagens = []
    videos = []
    others = []
    directories = []
    for entry in scandir_obj:
        file_path = force_bytes(entry.path).decode('utf8', 'surrogateescape')

        if entry.is_file():
            file_path = file_path.replace(obj_path.path_root,
                                          obj_path.path_url)
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
                "path": file_path.replace(obj_path.path_root, "")
            })

    context = {
        "active": "file_serve",
        "path_slug": path_slug,
        "path_name": path_name,
        "obj_path": obj_path,
        "path_back": path.dirname(path_name),
        "local_name": path_name.split("/")[-1],
        "directories": sorted(directories, key=lambda k: k['name']),
        "directories_length": len(directories),
        "imagens": sorted(imagens, key=lambda k: k['name']),
        "imagens_length": len(imagens),
        "videos": sorted(videos, key=lambda k: k['name']),
        "videos_length": len(videos),
        "others": sorted(others, key=lambda k: k['name']),
        "others_length": len(others),
    }

    return render(request, template_name, context)
