import requests


# Находим героев из заданного списка Heroes_names по заданной powerstat
def get_heroes(heroes_names, powerstat):
	base_url = 'https://akabab.github.io/superhero-api/api/all.json'
	responce = requests.get(base_url)
# На выходе получаем словарь из героев и их сил
	heroes = {i['name']: i["powerstats"][powerstat] for i in responce.json() if i['name'] in heroes_names}
	return heroes


# Находим самого по заданной силе
def find_max(heroes):
	v, k = max((v, k) for k, v in heroes.items())
	return k, v


if __name__ == "__main__":
	heroes_names = ['Hulk', 'Captain America', 'Thanos']
	powerstat = 'intelligence'
	heroes_list = get_heroes(heroes_names, powerstat)
	best_hero = find_max(heroes_list)
	print(f"The best hero is {best_hero[0]} with {powerstat} = {best_hero[1]}")
