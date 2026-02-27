import urllib.request

url = 'https://raw.githubusercontent.com/AllenDowney/ThinkPython/v3/words.txt'
urllib.request.urlretrieve(url, 'data/words.txt')