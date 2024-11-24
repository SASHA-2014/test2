print("A text")
from bs4 import BeautifulSoup
import requests
response = requests.get("https://coinmarketcap.com/")
soup = BeautifulSoup(response.text, features="html.parser")
coins = [soup.find_all('p', {"class": "georgia, bookman old style, palatino linotype, book antiqua, palatino, trebuchet ms, helvetica, garamond, sans-serif, arial, verdana, avante garde, century gothic, comic sans ms, times, times new roman, serif"})]
file = open("coins,txt", 'w')
for i in range(0, len(coins[0])):
    print(f"{coins[0][i].text} {coins[1][i].text} {coins[2][i].text}")
    file.write(f"{coins[0][i].text} {coins[1][i].text}\n")

file.close()
