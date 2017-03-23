
from django import template
from django.conf import settings
from django.utils.encoding import force_bytes
from os import scandir, path

register = template.Library()


@register.filter(name="back_directories")
def back_directories(dir_path):
    directories = []
    local_path = path.join(settings.FILE_PATH_ROOT, dir_path)

    for entry in scandir(local_path):
        file_path = force_bytes(entry.path).decode('utf8', 'surrogateescape')

        if entry.is_dir():
            directories.append({
                "name": entry.name,
                "path": file_path.replace(settings.FILE_PATH_ROOT, "")
            })
    return directories


@register.filter(name="get_back_path")
def get_back_path(dir_path):
    return path.dirname(dir_path)


@register.filter(name="active_pach")
def active_pach(path_now, dir_path):
    if path_now == dir_path:
        return 'active'
    return ''
