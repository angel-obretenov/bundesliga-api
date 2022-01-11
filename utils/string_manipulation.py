import re

pattern = re.compile(r'(?<!^)(?=[A-Z])')


# groupID goes to group_order_i_d, so decided not to use it
def dict_camel_to_snake(items: dict):
    new_dict = {}

    for key in items.keys():
        new_dict[pattern.sub('_', key).lower()] = items[key]

    return new_dict
