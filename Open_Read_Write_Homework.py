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