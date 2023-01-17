import requests
from bs4 import BeautifulSoup
from sklearn import datasets

#1 на базе данных введенных вручную
print("Введите числа через пробел:")
a = list(map(int, input().split()))
print(list(a))

#2 на базе данных полученных при парсинге
url = 'https://www.statisticbrain.com/fun-facts/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
table = soup.find('table', cellspacing="0", cellpadding="2")
td_all = table.find_all('td')
fact_list = list(map(lambda temp: temp.contents[0], td_all))
fact_list.pop(0)
print(fact_list)

# 3 на базе данных из датасета
iris = datasets.load_iris()
listic = list(iris.target_names)
print(listic)
x = map(len, listic)
print(list(x))