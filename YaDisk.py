import requests
from pprint import pprint


class YaUploader:
	def __init__(self, token):
		self.token = token

	# file_path: str
	def upload(self):
		upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
		headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
		params = {"path": '', "overwrite": "true"}
		response = requests.get(upload_url, headers=headers, params=params)
		print(response)

	# def get_files_list(self):
	# 	files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
	# 	headers = self.get_headers()
	# 	response = requests.get(files_url, headers=headers)
	# 	return response.json()

	# def _get_upload_link(self, disk_path):
	# 	upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
	# 	headers = self.get_headers()
	#
	# 	response = requests.get(upload_url, headers=headers, params=params)
	# 	pprint(response.json())
	# 	return response.json()
	#
	# def upload_files(self, disk_path, file_name):
	# 	result = self._get_upload_link(disk_path=disk_path)
	# 	href = result.get('href', '')
	# 	response = requests.put(href, data=open(file_name, 'rb'))
	# 	response.raise_for_status()
	# 	if response.status_code == 201:
	# 		print("Success")



TOKEN = 'y0_AgAAAAAAlde3AADLWwAAAADTHHzbYD0Iis_mQIyLneHfVdTHZJwtbnw'
ya = YaUploader(token=TOKEN)
ya.upload()


