from bs4 import BeautifulSoup
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
Web=requests.get("https://www.website-name.com", headers=headers)

soup=BeautifulSoup(Web.text, "html.parser")
counter=0

for link in soup.findAll('a', class_="enter-class-here"):
    #site="https://www.website-name.com"
    #await context.bot.send_message(chat_id=update.effective_chat.id, text= site+link.a['href'])
    print(link['href'])
    counter+=1

    if counter > 10:
        break
