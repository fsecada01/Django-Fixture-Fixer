import os
import json
import csv


class FileObject:
    def __init__(self, file_path):
        self.file = file_path
        self.name = os.path.basename(file_path).split('.')[:-1][0]
        self.dir = os.path.dirname(file_path)
        self.file_ext = self.file.split('.')[-1]
        self.data = None
        self.model = None

    def json_loader(self):
        if self.file_ext == 'json':
            with open(self.file, 'r+') as f:
                data = f.read()
                if len(data) == 0:
                    return "No data to sanitize."
                else:
                    data_json = json.loads(json.dumps(data))
                    data_json = [x for x in data_json.split('\n') if x != '']
                    data_json = [json.loads(x) for x in data_json]
                    [x.pop('_id') for x in data_json if x['_id']]

                    self.data = data_json
                    return "Json sanitation done!"
        else:
            return f"Your attached file is not JSON. Its extension is {self.file_ext}."

    def _file_name_changer(self, ext='csv'):
        base_file_name = os.path.basename(self.file)
        base_dir = os.path.dirname(self.file)
        parts = base_file_name.split('.')
        file_part = '_'.join([x for x in parts if x != parts[-1]])
        return '.'.join((os.path.join(base_dir, file_part), ext))

    def json_dump(self, file_dest=None):
        '''
        Dump sanitized JSON data into its own file. Useful for cleaning data
        coming from MongoDB.
        '''
        if self.data is None:
            self.json_loader()
        data = self.data

        if file_dest is None:
            dest = os.path.join(self.dir, 'sanitized',
                                f'{self.name}_sanitized.{self.file_ext}')
        else:
            dest = file_dest

        with open(dest, 'w') as f:
            json.dump(data, f, sort_keys=True, indent=4)

        return f"Wrote json to {dest}"

    def json_to_csv(self):
        '''
        This presumes a json data load. The function can be amended or
        modified to transform data into multiple file types, but the initial
        data must always be serialized JSON.
        '''
        if self.data is None:
            data = self.json_loader()
        else:
            data = self.data

        if len(data) == 0:
            pass
        else:

            heading = list(data[0].keys())
            values = [list(x.values()) for x in data]

            with open(f'{self._file_name_changer()}', 'w+', newline='') as f:
                writer = csv.writer(f, delimiter=',')
                writer.writerow(heading)
                [writer.writerow(x) for x in values]

            print(
                f'wrote {os.path.basename(file_name)} to {csv_file_name(file_name, ext)}!')
