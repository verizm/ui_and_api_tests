import pytest
import os
import shutil
import subprocess
import textwrap

import pytest
import datetime
import time
import random


#
# @pytest.fixture(scope="session")
# def add_to_cashe(request):
#     key = "path/duration"
#     request.config.cache.set("Name", "Vasia")
#
# #
# # @pytest.fixture
# # def get_from_cache(request):
# #     return request.config.cache.get("Name", None)
#
#
# def test_python_version(add_to_cashe):
#     assert "Vasia" == add_to_cashe


@pytest.fixture(autouse=True)
def check_duration(request, cache):
    folder = "/test_cache"


    # идентификатор узла (nodeid) может иметь двоеточия
    # ключи становятся именами файлов внутри .cache
    # меняем двоеточия на что-то безопасное в имени файла=
    url = "qweuqwioeuoqweio"
    cache.set("/main", url)
    yield url









@pytest.mark.parametrize('i', range(5))
def test_slow_stuff(i, check_duration):
    print(check_duration)

