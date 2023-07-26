# Telegram Article Scraper Bot
Code that allows a Telegram bot to scrape article links from a website using [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) and sends it to your chat. 

##### Features:
- 🎨 Customizable - You can pretty much try any publication site (some do block web scraping).
- ⚡ Quick & efficient - The scraper pulls articles very quickly and sends it directly to your chat.
- 📰 Article previews - Telegram does a great job displaying a preview of the article link in the chat.

##### Screenshots:
<img src="https://user-images.githubusercontent.com/122472324/256364284-3fef98f6-8a4f-4b87-a0af-1121b52bc2e7.jpeg" width=30% height=30% alt="screenshot1"> 
<img src="https://user-images.githubusercontent.com/122472324/256364288-adc128e6-1f3b-44d5-87bd-333749e06a91.jpeg" width=30% height=30% alt="screenshot2">

## Instructions 
1. Use a device that can run 24/7, like a Raspberry Pi.
2. Install Python and [Telegram's Python Bot code](https://github.com/python-telegram-bot/python-telegram-bot) on said device.
3. Use Telegram's [BotFather](https://core.telegram.org/bots/tutorial) to create a new bot. Put the API token in your Python file.
4. Find the publication site(s) you want to pull articles from and identify the article div class name. I suggest using a browser's inspection feature.
5. Edit the Python file to include the website, the article div class, and the href into the function to pull the article links.
6. Run the bot and see if you can scrape the URLs of the articles. _(Use the 'test.py' file if you just want to test the web scraper first before entering anything into the Telegram bot code)._
7. 📚 👓 Enjoy! 

## Examples:

##### PC Gamer
```python3
async def pcgamer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Let's go!")

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
    Web=requests.get("https://www.pcgamer.com/news/", headers=headers)

    soup=BeautifulSoup(Web.text, "html.parser")
    counter=0

    for link in soup.findAll('a', class_="article-link"):
        await context.bot.send_message(chat_id=update.effective_chat.id, text= link['href']) #send the href to the chat
        counter+=1

        if counter > 10: #Pull only 10 articles
            break
```
##### Reuters World News

```python3
async def reuters(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Here are the current events")

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
    Web=requests.get("https://www.reuters.com/world/", headers=headers)

    soup=BeautifulSoup(Web.text, "html.parser")
    counter=0

    for link in soup.findAll('a', class_="text__text__1FZLe text__dark-grey__3Ml43 text__inherit-font__1Y8w3 text__inherit-size__1DZJi link__underline_on_hover__2zGL4 media-story-card__heading__eqhp9"):
        site="https://www.reuters.com"
        await context.bot.send_message(chat_id=update.effective_chat.id, text= site+link['href']) #adding the href to the end of www.reuters.com
        counter+=1

        if counter > 10:
            break
```
## Questions?
Feel free to post in the Discussions or Issues tabs. 
