from websites_manager.core.models import FilePathModel


def get_file_path(request):
    return {"file_paths": FilePathModel.objects.all()}
