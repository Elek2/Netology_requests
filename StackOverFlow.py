import requests
from pprint import pprint
import datetime


def questions(todate, fromdate):
	url = r'https://api.stackexchange.com/2.3/questions'
	params = {
		"fromdate": fromdate,
		"todate": todate,
		"order": "desc",
		"site": "stackoverflow",
		"tagged": "python",
		"sort": "activity"
		}
	response = requests.get(url, params=params)
	question = {i['owner']['display_name']: i["link"] for i in response.json()['items']}
	pprint(question)


if __name__ == '__main__':
	# Устанавливаем нужные дату и время и переводим в формат timespamp
	now = datetime.datetime.utcnow()
	delta = datetime.timedelta(days=2)
	stamp_now = int(now.timestamp())
	stamp_before = int((now - delta).timestamp())

	questions(stamp_now, stamp_before)
