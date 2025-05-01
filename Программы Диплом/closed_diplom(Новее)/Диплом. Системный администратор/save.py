# from pywebcopy import save_webpage, save_website
# import validators

# def warning(text):
# 	print("\033[1m\033[31m{}\033[0m".format(text))

# def webpage(url, folder, name):
# 	save_webpage(
# 		url=url,
# 		project_folder=folder,
# 		project_name=name,
# 		bypass_robots=True,
# 		debug=True,
# 		open_in_browser=True,
# 		delay=None,
# 		threaded=False,
# 	)

# def website(url, folder, name):
# 	save_website(
# 		url=url,
# 		project_folder=folder,
# 		project_name=name,
# 		bypass_robots=True,
# 		debug=True,
# 		open_in_browser=True,
# 		delay=None,
# 		threaded=False,
# 	)

# print("""Выберите цифру:
# 1 - Сохранить страницу
# 2 - Сохранить сайт""")
# b=False

# while b==False:
# 	try:
# 		a = int(input())
# 		if a==1 or a==2:
# 			b=True
# 		else:
# 			warning("Выберите корректный номер!")
# 	except:
# 		warning("Только цифры!")

# c=False
# while c==False:
# 	url = input("Введите ссылку: ")
# 	if validators.url(url):
# 		c=True
# 	else:
# 		warning("Некорректная ссылка!")

# folder=input("Куда сохранять: ")
# name=input("Название проекта: ")
# if a==1:
# 	webpage(url, folder, name)
# else:
# 	website(url, folder, name)


#####################################

from pywebcopy import save_webpage

save_webpage(
		url="http://ege.fipi.ru/bank/questions.php?search=1&pagesize=10&proj=E040A72A1A3DABA14C90C97E0B6EE7DC&theme=&qlevel=&qkind=&qsstruct=&qpos=&qid=496A40&zid=&solved=&favorite=&blind=",
		# url="https://httpbin.org",
		project_folder="C://Users//Nolic//Desktop//Сайт//",
		project_name="test",
		bypass_robots=True,
		debug=False,
		open_in_browser=True,
		delay=None,
		threaded=False,
	)

##############################################

# from pywebcopy import save_webpage

# url = 'https://dzen.ru/?yredirect=true&clid=2261452&win=553'
# download_folder = 'C://Users//Nolic//Desktop//Сайт//'  #'/path/to/downloads/'    

# kwargs = {'bypass_robots': True, 'project_name': 'recognisable-name'}

# save_webpage(url, download_folder, **kwargs)