def get_data_fig(*args, **kwargs):
    res = []
    res.append(sum(args))
    if 'type' in kwargs.keys():
        res.append(kwargs.get('type'))
    if 'color' in kwargs.keys():
        res.append(kwargs.get('color'))
    if 'closed' in kwargs.keys():
        res.append(kwargs.get('closed'))
    if 'width' in kwargs.keys():
        res.append(kwargs.get('width'))
    return tuple(res)


print(get_data_fig(5, 4, 9, 9, 9, 9, type=False, color='Yellow', closed=True, width=10))
print(get_data_fig(5, 4, 9, 9, 9, 9, color='Yellow', type=False, closed=True, width=10))
print(get_data_fig(5, 4, color='Yellow', type=False, closed=True))

# ПРАВИЛЬНЫЙ РЕЗУЛЬТАТ:
#
# (45, False, 'Yellow', True, 10)
# (45, False, 'Yellow', True, 10)
# (9, False, 'Yellow', True)
