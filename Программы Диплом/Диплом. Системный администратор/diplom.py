# Импорт библиотек

import requests
import re
import random

# Очистка html от тегов

CLEANHTML = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
def cleanhtml(raw_html):
  cleantext = re.sub(CLEANHTML, '', raw_html)
  return cleantext

list = 9094

sections_array = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7]#, 1.8]
number = '4FF344'
finder = 'Номер: '

result = ''



for i in range (len(sections_array)):
    start = -1
    count = 0
    end = -1
    
    link_one = f"http://ege.fipi.ru/bank/questions.php?search=1&pagesize={list}&proj=E040A72A1A3DABA14C90C97E0B6EE7DC&theme={sections_array[i]}&qlevel=&qkind=&qsstruct=&qpos=&qid=&zid=&solved=&favorite=&blind="
    req = requests.get(link_one)
    src = req.text
    
    lister = []
    
    while True:
        start = src.find('Номер: ', start+1)
        if start == -1:
            break
        end = start + 31
        # print(end)
        count += 1
        lister.append(end)
    
    print("Количество вхождений символа в строку: ", count )
    print(f'{sections_array[i]} {list}')
    test = ''
    for i in range(len(lister)):
        for j in range (6):
        # print(req.text[list[i]+j])
            test += req.text[lister[i]+j]
        test+=' '
    test = test.split(" ")
    
    rand = random.randint(0,count-1)
    
    print(test[rand])
    
    number = test[rand]
    
    link_two = f"http://ege.fipi.ru/bank/questions.php?search=1&pagesize=10&proj=E040A72A1A3DABA14C90C97E0B6EE7DC&theme=&qlevel=&qkind=&qsstruct=&qpos=&qid={number}&zid=&solved=&favorite=&blind="
    # link_two = f"http://ege.fipi.ru/bank/questions.php?search=1&pagesize=10&proj=E040A72A1A3DABA14C90C97E0B6EE7DC&theme=&qlevel=&qkind=&qsstruct=&qpos=&qid=4CB472&zid=&solved=&favorite=&blind="
    
    req = requests.get(link_two)
    src = req.text
    
    print(src)
    tester = ''
    
    tester = re.search('<p class="MsoNormal">(.+?)</p>', src)
    if tester:
        tester = tester.group(1)
    else:
        tester = re.search('<P class=Basis><SPAN>(.+?)</P>', src)
        if tester:
            tester = tester.group(1)
        else:
            tester = re.search('<p class=MsoNormal>(.+?)</p>', src).group(1)
        
    
    # .group(1)
    
    print('\n')
    tester = tester.replace('m:', '')
    tester = tester.replace('math', 'math xmlns="http://www.w3.org/1998/Math/MathML"')
    
    result += f'<p class="MsoNormal">{tester}</p>'
    result += '\n'
    print('\n')
    
text = f'<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>Document</title>\n</head>\n<body>\n{result}\n</body>\n</html>'
print(text)

with open("hello.html", "w", encoding="utf-8") as file:
    file.write(text)
    print("Файл записан")
    