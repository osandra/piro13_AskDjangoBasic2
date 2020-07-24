import os
from uuid import uuid4


def uuid_upload_to(instance, filename):
    uuid_name = uuid4().hex
    ext = os.path.splitext(filename)[-1].lower()
    return '/'.join([
        uuid_name[:2],  # 처음 2글자. 16진수 -> 256가지 조합
        uuid_name[2:4],
        uuid_name[4:] + ext
    ])