
from django import template
from django.utils.encoding import force_bytes
from os import scandir, path

register = template.Library()


@register.filter(name="back_directories")
def back_directories(path_root, dir_path):
    directories = []

    local_path = path.join(path_root, dir_path)

    for entry in scandir(local_path):
        file_path = force_bytes(entry.path).decode('utf8', 'surrogateescape')

        if entry.is_dir():
            directories.append({
                "name": entry.name,
                "path": file_path.replace(path_root, "")
            })
    return sorted(directories, key=lambda k: k['name']),


@register.filter(name="get_back_path")
def get_back_path(dir_path):
    return path.dirname(dir_path)


@register.filter(name="active_pach")
def active_pach(path_now, dir_path):
    if path_now == dir_path:
        return 'active'
    return ''
