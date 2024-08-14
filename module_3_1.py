#Функция count_calls подсчитывающая вызовы остальных функций.
#Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки,
# строку в верхнем регистре, строку в нижнем регистре.
#Функция is_contains принимает два аргумента: строку и список, и возвращает True, если
# строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
calls = 0



def count_calls():         # подсчитывающая вызовы остальных функций.
    global calls
    calls += 1


def string_info(string):
    count_calls()
    print(len(string), string.upper(), string.lower())
    #print(string.upper())
    #print(string.lower())


def is_contains(string, list_to_search):
    count_calls()
    b = string in list_to_search
    print(b)


string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN']) # Urban ~ urBAN
is_contains('cycle', ['recycling', 'cyclic']) # No matches
print(calls)

