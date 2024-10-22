from pprint import pprint


def introspection_info(obj):
    type1 = type(obj)
    dir_1 = dir(obj)
    attr = []
    meth = []
    obj_info = {'type': type1, 'attributes': attr, 'methods': meth, 'module': type1}
    for item in dir_1:
        if item[0] == '_':
            attr.append(item)
        if item[0] != '_':
            meth.append(item)
    return obj_info


info = introspection_info(42)
pprint(info)
