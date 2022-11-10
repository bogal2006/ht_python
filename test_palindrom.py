import pytest

def check_palindrom(string_: str):
    """Функция убирает пробелы и 
    переводит символы в нижний регистр в строке
    затем проверяет ее на валидность палиндрома
    и в зависимости от этого возвращает сообщение"""
    a=string_.lower().strip()
    if a==a[::-1]:
        return 'строка есть палиндром'
    else:
        return 'строка не полиндром'


# тестирование функции если строка палиндром
@pytest.mark.parametrize('string_,palindrom', [('топот','строка есть палиндром'),('sos','строка есть палиндром'),('Казак','строка есть палиндром')])
def test_check_palindrom(string_, palindrom):
    assert check_palindrom(string_)==palindrom
    
# тестирование функции если строка не палиндром
@pytest.mark.parametrize('string_2, not_palindrom', [('ропот','строка не полиндром'), (' ЦокоТ','строка не полиндром'),('gor','строка не полиндром')]) 
def test_not_check_palindrom(string_2, not_palindrom):
     assert check_palindrom(string_2)==not_palindrom                                             
                                 




