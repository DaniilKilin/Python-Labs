import requests
from bs4 import BeautifulSoup
from sklearn import datasets

#1 на базе данных введенных вручную
print("Введите числа через пробел:")
a = list(map(int, input().split()))
print(list(a))

#2 на базе данных полученных при парсинге
url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
fact_list = list(map(lambda temp: temp.contents[0], quotes))
print(fact_list)

# 3 на базе данных из датасета
iris = datasets.load_iris()
listic = list(iris.target_names)
print(listic)
x = map(len, listic)
print(list(x))
