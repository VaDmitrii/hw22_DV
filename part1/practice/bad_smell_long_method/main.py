# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    data = _read(data=csv)
    data_sorted = _sort(data=data)
    return _filter(data_sorted=data_sorted)


def _read(data):
    return [line.split(';') for line in data.split('\n')]


def _sort(data):
    return sorted(data, key=lambda item: int(item[1]))


def _filter(data_sorted):
    return [item for item in data_sorted if int(item[1]) > 10]


if __name__ == '__main__':
    print(get_users_list())
