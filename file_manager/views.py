import os
from pathlib import Path
import shutil
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK


@api_view(['GET'])
def get_directory(request):
    params = request.query_params
    current_dir = str(Path.home())
    if params.get('dir'):
        current_dir = params.get('dir')

    return Response(
        {
            'dir': current_dir,
            'list': os.listdir(current_dir)
        }
        , status=HTTP_200_OK)


@api_view(['POST'])
def open_file(request):
    file_path = request.query_params.get('path')
    print(file_path)
    os.system('open ' + file_path)

    return Response(status=HTTP_200_OK)


@api_view(['POST'])
def rename_file_or_folder(request):
    params = request.query_params
    old_path = params.get('old_path')
    new_path = params.get('new_path')

    os.rename(old_path, new_path)

    return Response(status=HTTP_200_OK)


@api_view(['POST'])
def copy_file_or_folder(request):
    params = request.query_params
    original_path = params.get('original_path')
    destination_path = params.get('destination_path')

    if os.path.isfile(original_path):
        shutil.copy(original_path, destination_path)
    else:
        shutil.copytree(original_path, destination_path)

    return Response(status=HTTP_200_OK)


@api_view(['POST'])
def move_file_or_folder(request):
    params = request.query_params
    original_path = params.get('original_path')
    destination_path = params.get('destination_path')

    shutil.move(original_path, destination_path)

    return Response(status=HTTP_200_OK)


@api_view(['GET'])
def get_path_stat(request):
    path = request.query_params.get('path')
    print(os.stat(path))
    s_obj = os.stat(path)
    # print(type(os.stat(path)))
    print({k: getattr(s_obj, k) for k in dir(s_obj) if k.startswith('st_')})
    return Response({k: getattr(s_obj, k) for k in dir(s_obj) if k.startswith('st_')}
    ,status=HTTP_200_OK)
