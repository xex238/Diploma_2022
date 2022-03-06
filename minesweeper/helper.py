import persistent
import re
import ZODB, ZODB.FileStorage
import transaction

class My_class:
    def __init__(self):
        self.data = [] # Данные
        self.processing_type = [] # Как обработать
        self.result = None # С чем сверить

    def __init__(self, data, processing_type, result):
        self.data = data # Данные
        self.processing_type = processing_type # Как обработать
        self.result = result # С чем сверить

    def processing(self):
        result = self.data[0]
        for i in range(len(self.processing_type)):
            if(self.processing_type[i] == 'sum'):
                result = self.sum(result, self.data[i + 1])
            elif(self.processing_type[i] == 'multiply'):
                result = self.multiply(result, self.data[i + 1])

        if(result == self.result):
            return True
        else:
            return False

    def sum(self, x1, x2):
        return x1 + x2

    def multiply(self, x1, x2):
        return x1 * x2
class My_class2:
    def __init__(self):
        self.x1 = 5
        self.x2 = 10

    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def my_method(x1, x2):
        return x1 + x2

class Account(persistent.Persistent):
    def __init__(self):
        self.balance = 0.0
    def deposit(self, amount):
        self.balance += amount
    def cash(self, amount):
        assert amount < self.balance
        self.balance -= amount

def method1():
    ss = ['Мама', 'авТо', 'гриБ', 'Яблоко', 'яБлоко', 'ябЛоко', 'яблОко', 'яблоКо', 'яблокО']

    for i in range(len(ss)):
        s = ss[i]
        match = re.search(r'^[а-я]*[А-Я]{1}[а-я]*$', s)
        match2 = re.match(r'[а-я]*[А-Я]{1}[а-я]*', s)

        print(match.string)
        # print(match2.group())
        # print(match2)

        if(ss[i] != match.string):
            print('Ошибка!')
            break

        '''
        if(match2):
            print(match2.group())
        else:
            print('Совпадений нет')
        '''

    ss = ['агент007', 'стриж', 'ГТО', 'Три богатыря']

    for i in range(len(ss)):
        s = ss[i]
        match = re.search(r'^[а-я]*[А-Я]{1}[а-я]*$', s)
        match2 = re.match(r'[а-я]*[А-Я]{1}[а-я]*', s)

        print(match)
        # print(match2.group())
        # print(match2)

        if((match != None) and (match.string != ss[i])):
            print('Ошибка!')
            break

        '''
        if(match2):
            print(match2.group())
        else:
            print('Совпадений нет')
        '''
def method2():
    s = []
    ss = [1, 2, 3]
    s.append(ss)
    ss1 = [4, 5, 6]
    s.append(ss1)
    print(s[0][0])
def method3():
    numbers = [1, 2, 3, 4, 5]

    for counter, item in enumerate(numbers):
        if(counter % 2 == 0):
            print(item)

    print(counter)
def method4():
    # Проверка соответствия значения его типу
    print(isinstance(1, int))
def method5():
    db_name = 'mydata.fs'

    # storage = ZODB.FileStorage.FileStorage(db_name)
    # db = ZODB.DB(storage)

    db = ZODB.DB(db_name)
    conn = db.open()

    root = conn.root()
    print(root.account1)
    root.account1 = Account()
    transaction.commit()
    print(root.account1)
    print(root.account1.balance)

    db.close()

# method1()
# method2()
# method3()
# method4()
method5()
