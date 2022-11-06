import requests
from pprint import pprint


class YaUploader:
	def __init__(self, token):
		self.token = token

	def upload(self, file_path: str):
		upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
		headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
		file_name = file_path.split("\\")[-1]
		params = {"path": file_name, "overwrite": True}
		response = requests.get(upload_url, headers=headers, params=params)
		pprint(response.json())
		disk_link = response.json()['href']
		return requests.put(disk_link, open(file_name, 'rb'))


if __name__ == '__main__':
	# Получить путь к загружаемому файлу и токен от пользователя
	path_to_file = r''
	token = ''
	uploader = YaUploader(token)
	result = uploader.upload(path_to_file)
	print(result)
