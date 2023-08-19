# Задача 1
with open('recipes.txt', 'rt') as file:
		cook_book = {}
		for l in file:
			department_name = l.strip()
			dictik = []
			listik = {}
			employees_count = file.readline()
			for i in range(int(employees_count)):
				emp = file.readline()
				ingredient_name, quantity, measure  = emp.strip().split(' | ')
				dictik.append({'ingredient_name': ingredient_name, 'quantity': quantity,'measure': measure})
				dep = {department_name: dictik}
			blank_line = file.readline()
			cook_book.update(dep)
# print(f'cook_book = {cook_book}')

# Задача 2
def get_shop_list_by_dishes(dishes, person_count):
  result = {}
  for dish in dishes:
    if dish in cook_book:
      for consist in cook_book[dish]:
        if consist['product'] in result:
          result[consist['product']]['quantity'] += int(consist['quantity']) * person_count
        else:
          result[consist['product']] = {'measure': consist['measure'], 'quantity': (int(consist['quantity']) * person_count)}
    else:
      print('Такого блюда нет в книге')
  print(result)
get_shop_list_by_dishes(['Запеченный картофель', 'Запеченный картофель'], 2)

# Задача 3
from operator import itemgetter

def number_of_line(*files):
	list_of_files = []
	text_f = []		
	for file in files:
		with open(file, encoding = 'utf-8') as file_obj:
			text_f = file_obj.read().splitlines()
			file_length = len(text_f)
			name_file = file
			list_of_files.append([name_file, file_length, text_f])
			list_of_files.sort(key = itemgetter(1))
	print(list_of_files)
	return list_of_files

number_line = number_of_line('1.txt', '2.txt', '3.txt')
a = '4.txt'

def writing_file(list_of_files,a):
	with open('4.txt', 'w', encoding='utf-8') as file_obj:
		for file in list_of_files:
			for element in file:
				file_obj.write(f'{element}\n')			
	file_path = '4.txt'
	return file_path
	
print(writing_file(number_line, '4.txt'))