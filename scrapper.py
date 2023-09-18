import requests
from bs4 import BeautifulSoup

req = requests.get("https://medium.com/@annarhysa13/comparative-analysis-of-rare-word-handling-strategies-in-text-summarization-models-f7b23354c7cb")

#file = open("text_file.txt", "r")
#contents = file.read()
soup = BeautifulSoup(req.content, "html.parser")
#res = soup.title

f = open("Healthy_affairs.txt", "w")
f.writelines(soup.get_text())
f.close()
#print(soup.get_text())
#print(res.prettify())