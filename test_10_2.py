
class Employee:
    def __init__(self, name, seniority):
        self.name = name
        self.seniority = seniority
        
        self.grade = 1
    
    def grade_up(self):
        """Повышает уровень сотрудника"""
        self.grade += 1
    
    def publish_grade(self):
        """Публикация результатов аккредитации сотрудников"""
        print(self.name, self.grade)
    
    def check_if_it_is_time_for_upgrade(self):
        pass
    
class Designer(Employee):
    def __init__(self, name, seniority,international_award=2): # дизайнер изначально имеет 2 премии
        super().__init__(name, seniority)
        self.international_award=international_award
        """ добавление по 2 балла за 1 премию """ 
        self.seniority=self.international_award*2+self.seniority
    
    def check_if_it_is_time_for_upgrade(self):
        
        # для каждой аккредитации увеличиваем счетчик на 1
        # пока считаем, что все дизайнеры проходят аккредитацию
        self.seniority+=1
        
        # условие повышения сотрудника после 7 баллов
        if self.seniority % 7 == 0:
            self.grade_up()
        
        # публикация результатов
        return self.publish_grade()
class Developer(Employee):
    def __init__(self, name, seniority):
        super().__init__(name, seniority)
    
    def check_if_it_is_time_for_upgrade(self):
        # для каждой аккредитации увеличиваем счетчик на 1
        # пока считаем, что все разработчики проходят аккредитацию
        self.seniority += 1
        
        # условие повышения сотрудника из презентации
        if self.seniority % 5 == 0:
            self.grade_up()
        
        # публикация результатов
        return self.publish_grade()
    

import pytest

@pytest.fixture
def designer_fixture():
    NAME_DESIGNER='Сергей'
    def _init_designer(seniority):
            return Designer(NAME_DESIGNER,seniority=seniority)
    return _init_designer

@pytest.fixture
def developer_fixture():
    NAME_DEVELOPER='Aleksey'
    def _init_developer(seniority):
        return Developer(NAME_DEVELOPER,seniority=seniority)
    return _init_developer
    
@pytest.mark.parametrize('enter,exeption',[(0,1),(4,2),(9,3),(14,4)])
def test_developer_metod(developer_fixture,enter,exeption):
    dev=developer_fixture(2)
    for i in range(enter):
        dev.check_if_it_is_time_for_upgrade()
    assert dev.grade==exeption        

@pytest.mark.parametrize('enter,exeption',[(0,1),(1,2),(2,2),(9,3)])
def test_designer_metod(designer_fixture,enter,exeption):
    des=designer_fixture(2)
    for i in range(enter):
        des.check_if_it_is_time_for_upgrade()
    assert des.grade==exeption 
    
    
   
    
    





    



