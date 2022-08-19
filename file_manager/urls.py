from rest_framework.urls import path

from .views import get_directory, open_file, rename_file_or_folder, copy_file_or_folder, move_file_or_folder, get_path_stat

urlpatterns = [
    path('file-manager/get-directory', get_directory, name='get_directory'),
    path('file-manager/open-file', open_file, name='open_file'),
    path('file-manager/rename', rename_file_or_folder, name='rename_file_or_folder'),
    path('file-manager/copy', copy_file_or_folder, name='copy_file_or_folder'),
    path('file-manager/move', move_file_or_folder, name='move_file_or_folder'),
    path('file-manager/path-stat', get_path_stat, name='get_path_stat'),
]
