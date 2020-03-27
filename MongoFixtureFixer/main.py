import os
import json
import csv
from .core.core import FileObject
from .core.data_transforming import *


# curr_path = os.getcwd()
# backup_path = os.path.join(curr_path, '..', '..', 'backups')
# backup_path = os.path.abspath(backup_path)

# files = []
# files_gen = os.walk(backup_path)
# files = list(files_gen)
# json_files = [os.path.join(backup_path, x)
#               for x in files[0][2] if 'json' in x and '__schema__' not in x]


# file_objs = [FileObject(x) for x in json_files]

# [x.json_dump() for x in file_objs]

# [x.json_loader() for x in file_objs]

# payload = [x for x in file_objs if x.data is not None]

# for x in payload:
#     x.data = data_trans(x.data, model_name=model_finder(x.name))

# model_names = set([y.get('model') for x in payload for y in x.data])

# model_names

# [x.json_dump() for x in payload]

# [x.data for x in payload]

# set([y.get('model') for x in payload for y in x.data])