def model_finder(base_file):
    parts = [x.lower() for x in base_file.lower().split('_')]
    model = '.'.join(parts)
    return model


def name_reducer(model_name):
    words = model_name.split('.')
    while len(words) > 2:
        words = words[1:]
    return '.'.join(words)


def data_trans(dict_obj, model_name):
    list_obj = []
    for x in dict_obj:
        new_dict = {}
        new_dict['model'] = model_name
        id_num = x.get('id') or x.get('ID')
        new_dict['pk'] = id_num
        if x.get('id') is not None:
            x.pop('id')
        elif x.get('ID') is not None:
            x.pop('ID')
        else:
            continue
        new_dict['fields'] = x
        list_obj.append(new_dict)
    return list_obj


def model_search(x, dict_list):
    for dict_obj in dict_list:
        if x in dict_obj:
            x = dict_obj.get(x)
            return x


def get_model_names():
    '''
    This function processes a list of model names from a json payload and
    compares it to existing models within a django project. This is done by
    converting the list of model instances into string representations and
    then sanitizing the string data.
    This is then compared against the model list and returns the true model
    name value for data transformation.
    '''

    from django.apps import apps

    model_list = apps.get_models()

    def _obj_str_conv(obj_list):
        raw_list = str(obj_list).split('<class ')
        unwanted_chars = ['>', '\'', ',', ' ', '[', ']', '\"']
        filter_list = [filter(lambda i: i not in unwanted_chars, x)
                       for x in raw_list]
        processed_list = [''.join(list(x)) for x in filter_list]
        return [x for x in processed_list if x != '' or None]

    model_names = _obj_str_conv(model_list)

    unwanted = ['core', 'applications', 'models', 'django', 'contrib']

    list_obj = []
    for x in model_names:
        split_words = x.split('.')
        new_words = '.'.join(y for y in split_words if y not in unwanted)
        list_obj.append(name_reducer(new_words))
        # list_obj.append(_name_reducer(new_words))

    return list_obj


def model_dict_creator(list_obj):
    # now to create the dictionary model:
    return [{x.lower(): x} for x in list_obj]
