class Book:
    author=''
    name=''
    count=0
DataBase=[]
def ReadDatabase():
    a= 'C:/Users/u/Desktop/dd.csv'
    global k
    k=0
    with open(a) as f:
        for line in f:
            DataBase.append(Book())
            a, b, c = line.strip().split(';')
            DataBase[k].author=a
            DataBase[k].name=b
            DataBase[k].count=int(c)
            k+=1     
    f.close()        
def ShowDatabase():
    for i in range(k):
        print(str(i+1) + ') ' + DataBase[i].author + ' "' + DataBase[i].name + '" ' + '[Кол-во: ' +str(DataBase[i].count)+']')
def AddDatabase():
    global k
    DataBase.append(Book())
    print('Введите автора книги', end='')
    DataBase[k].author=input()
    print('Введите название книги', end='')
    DataBase[k].name=input()
    print('Введите доступное кол-во книг', end='')
    DataBase[k].count=int(input()) 
    k+=1      
def DelDatabase():
    global k
    print('''Введите: 
    1 - для удаления по автору
    2 - для удаления по названию
    3 - для удаления по номеру в базе
    0 - для отмены''')
    mode=int(input())
    while mode not in [0,1,2,3]:
        print('Введите верное значение')
        mode=int(input())
    if mode==0:
        return
    elif mode==1:
        reqauthor=input('Введите нужного автора')
        flag=False  
        for i in range(k):
            if DataBase[i].author==reqauthor:
                flag=True
                del(DataBase[i])
                k-=1
        if not flag:
            print('Такого автора нет в базе данных')
    elif mode==2:
        reqname=input('Введите нужную книгу')
        flag=False  
        for i in range(k):
            if DataBase[i].name==reqname:
                flag=True
                del(DataBase[i])
                k-=1
        if not flag:
            print('Такой книги нет в базе данных')
    else:
        reqcount=int(input('Введите нужный номер'))
        while reqcount>k:
            print('Номера не сущетсвует')
            reqcount=int(input(' Введите коректный номер'))
        del(DataBase[reqcount-1])
        k-=1
def SaveDatabase():
    global k
    b=input('Введите путь к файлу, в котором хотите сохранить свою базу данных')
    while True:
        try:
            f=open(b, 'w+')
            break
        except:
            print('Неправильно указано расширение файла')
            b = input('Введите правильное расширение \n')
    with open(b, 'w+') as f:
        for i in range(k):
            f.write(DataBase[i].author + ';' + DataBase[i].name + ';'+ str(DataBase[i].count) + '\n')
    f.close()      
def SortDatabase():
    print('''Введите:
    1 - для сортировки по автору
    2 - для сортировки по названию книги
    3 - для сортировки по кол-ву книг''')
    mode=int(input())
    while True:
        if mode not in [1,2,3]:
            print('Введена некоректная команда')
            mode=int(input('Введите команду коректно'))
        else:
            break 
    if mode == 1:
        print('В алфавитном или обратном порядке (1/2)', end='')
        mode=int(input())
        while True:
            if mode not in [1,2]:
                print('Введите значение коректно')
                mode = int(input())
            else:
                break        
        if mode ==1:
            DataBase.sort(key=lambda x: x.author)
        elif mode == 2:
            DataBase.sort(key=lambda x: x.author, reverse=True)
    elif mode == 2:
        print('В алфавитном или обратном порядке (1/2)', end='')
        mode=int(input())
        while True:
            if mode not in [1,2]:
                print('Введите значение кореткно')
                mode = int(input())
            else:
                break 
        if mode ==1:
            DataBase.sort(key=lambda x: x.name)
        elif mode == 2:
            DataBase.sort(key=lambda x: x.name, reverse=True)
    else:
        print('По возрастанию или убыванию (1/2)', end='')
        mode=int(input())
        while True:
            if mode not in [1,2]:
                print('Введите значение коректно')
                mode = int(input())
            else:
                break 
        if mode ==1:
            DataBase.sort(key=lambda x: x.count)
        elif mode == 2:
            DataBase.sort(key=lambda x: x.count, reverse=True)   

cmd=0
lastcmd=0
print('Здраствуйте, Дмитрий Николаевич.Добро пожаловать в меню СУБД.')
ReadDatabase()
print('''Введите:
 -1 - для выхода из программы
 1 - для просмотра базы данных
 2 - для добавления новых элементов
 3 - для удаления элементов
 4 - для сохранения базы данных
 5 - для сортировки базы данных''')
while cmd != -1:
    try:
        cmd = int(input('Введите номер команды'))
    except:
        print('Введено не число')
        cmd=0  
    if cmd == 0:
        continue      
    if cmd == -1:
        if lastcmd==4:
            print('Работа окончена. До свидания')
            break
        else:
            answer = input('Работа с базой данных окончена, хотите сохранить её? (Y/N) ').lower()
            if answer=='Y':
                SaveDatabase()
            print('Работа окончена. До свидания')
            break
    elif cmd == 1:
        ShowDatabase()
        lastcmd=1  
    elif cmd == 2:
        AddDatabase()
        lastcmd=2  
    elif cmd == 3:
        DelDatabase()
        lastcmd=3
    elif cmd == 4:
        SaveDatabase()
        lastcmd=4 
    elif cmd == 5:
        SortDatabase()  
        lastcmd==5   
    else:
        print('Некоректный номер команды')