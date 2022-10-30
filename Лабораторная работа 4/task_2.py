def get_count_char(str_):
    dict_ = {}
    for s in str_.lower():
        if s.isalpha():
            if s in dict_:
                dict_[s] += 1
            else:
                dict_[s] = 1
    return dict_

def get_percent_char(dict_):
    sum_of_all_values =  sum(get_count_char(main_str).values())
    for key, value in dict_.items():
        dict_[key] = f"{round(value/222*100,2)} %"
    return dict_


main_str = """
Данное предложение будет разбиваться на отдельные слова.
В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов.
Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))

# new_dict = get_count_char(main_str)
# print(new_dict)
# print(get_percent_char(new_dict))
