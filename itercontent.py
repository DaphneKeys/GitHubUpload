import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
