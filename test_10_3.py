import requests
class Rate:
   
    def __init__(self, format_='value', diff=False):
        self.format = format_
        self.diff=diff      #добавлена переменная diff
    
    def exchange_rates(self):
        
        """
        Возвращает ответ сервиса с информацией о валютах в виде:
        
        {
            'AMD': {
                'CharCode': 'AMD',
                'ID': 'R01060',
                'Name': 'Армянских драмов',
                'Nominal': 100,
                'NumCode': '051',
                'Previous': 14.103,
                'Value': 14.0879
                },
            ...
        }
        """
        self.r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return self.r.json()['Valute']
    def make_format(self, currency):
        """
        Возвращает информацию о валюте currency в трех вариантах:
        - полная информация о валюте при self.format = 'full':
        Rate('full').make_format('EUR')
        {
            'CharCode': 'EUR',
            'ID': 'R01239',
            'Name': 'Евро',
            'Nominal': 1,
            'NumCode': '978',
            'Previous': 79.6765,
            'Value': 79.4966
        }
        
        Rate('value').make_format('EUR')
        79.4966
        
        Rate('value',True) выводит разницу с предыдущим курсом
        """
        response = self.exchange_rates()
        
        if currency in response:
            if self.format == 'full':
                return response[currency]
            
            if self.format == 'value' and self.diff==False:
                return response[currency]['Value']
            if self.format == 'value' and self.diff==True:
                return response [currency]['Value']-response [currency]['Previous']
        
        return 'Error'
    
    def eur(self):
        """Возвращает курс евро на сегодня в формате self.format"""
        return self.make_format('EUR')
    
    def usd(self):
        """Возвращает курс доллара на сегодня в формате self.format"""
        return self.make_format('USD')
    
    def brl(self):
        """Возвращает курс бразильского реала на сегодня в формате self.format"""
        return self.make_format('BRL')
    
    
    def max_exchange(self):
        """
        функция возвращающая название валюты с максимальным значением курса
        """
        
        name_max_exchange='' # переменная с названием валюты с максимальным курсом
        response = self.exchange_rates() # получаем словарь с курсами всех валют
        list_value_currency=[] # переменная списка курсов валют
        for k in response.keys():  # в цикле перебираем и записываем значения курса каждой валюты в список 
            list_value_currency.append(response.get(k)['Value']/response.get(k)['Nominal']) # для получения курса делим на номинал валюты
        max_exchange=max(list_value_currency) # получаем максимальное значение валюты из списка
        
        for k in response.keys():  # в цикле перебираем значения всех валют пока не будет совпадения с максимальным значением
            if response.get(k)['Value']==max_exchange:
                name_max_exchange=response.get(k)['Name'] # сохраняем название валюты с максимальным значением
                break
        return name_max_exchange
        
        
        
import pytest
@pytest.fixture
def rate_fixture():
    def _init_rate(format_,diff):
        return Rate(format_=format_,diff=diff)
    return _init_rate

full_value={
            'CharCode': 'EUR',
            'ID': 'R01239',
            'Name': 'Евро',
            'Nominal': 1,
            'NumCode':'978',
            'Previous':79.6765,
            'Value':79.4966
                }
@pytest.mark.parametrize('format_,diff,expected',[('full',False,full_value),('full',True,full_value),('value',False,79.4966),('value',True,-0.1799000000000035)])
def test_exchange(rate_fixture,mocker,format_,diff,expected):
    mocker.patch('test_10_3.Rate.exchange_rates',return_value={
            'EUR': {
            'CharCode': 'EUR',
            'ID': 'R01239',
            'Name': 'Евро',
            'Nominal': 1,
            'NumCode':'978',
            'Previous':79.6765,
            'Value': 79.4966
                }})    
    c=rate_fixture(format_,diff) 
    assert c.eur()==expected
   
