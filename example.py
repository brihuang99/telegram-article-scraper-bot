import logging
import requests
import re
from bs4 import BeautifulSoup
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

token="" #ENTER YOUR BOT'S API TOKEN HERE

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def scrape(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:   #defines the scraping function for the bot
    keyboard = [
        [InlineKeyboardButton("Site Name", callback_data="descriptor of site")], #Enter the name of the website and give it a name to reference in the query function below
        #ADD AS MANY AS YOU LIKE!

    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Enter a message for the bot to say", reply_markup=reply_markup) #This appears after the function is selected
    



async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: #
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(text=f"Selected option: {query.data}")

    if query.data == "descriptor of site":
    	await sitescrapefunction(update, context) #this calls the bot to scrape the relevant site


#BELOW IS ONE EXAMPLE OF HOW A WEBPAGE CAN BE SCRAPED. KEEP IN MIND EVERY WEBSITE IS DIFFERENT!! USE YOUR BROWSER TO INSPECT!!
async def sitescrapefunction(update: Update, context: ContextTypes.DEFAULT_TYPE): #this is the function to scrape a specific site. make sure that this matches what's in the query.data
    await context.bot.send_message(chat_id=update.effective_chat.id, text="bot message") #this tells the bot to send a message to the chat; you can include a little personalized message from the bot for each site scraped

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
    Web=requests.get("https://website-name-goes-here.com", headers=headers)

    soup=BeautifulSoup(Web.text, "html.parser")


    site="https://website-name-goes-here.com" #sometimes, scraping a webpage does not give the full URL, only the href. I made a variable for the beginning of the URL in case we need it.
    counter=0

    for link in soup.findAll('a', class_="class-goes-here"): #attempt to scrape the links in all divs with this class
        article=site + link['href'] #add the href to the site URL. KEEP IN MIND THAT THIS CAN VARY DEPENDING ON THE SITE VISITED!!!
        await context.bot.send_message(chat_id=update.effective_chat.id, text= article) #send the URL to the chat
        counter+=1

        if counter > 10: #i have the bot only pull 10 articles, but you can change this to whatever amount you want.
            break

    

if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()
    application.add_handler(CallbackQueryHandler(button))

    application.add_handler(CommandHandler("scrape", scrape)) #shows the scrape function in the bot chat window after tapping on menu

   sitescrapefunction = CommandHandler('sitescrapefunction', sitescrapefunction) #this defines the function for the bot, so it knows to run the scraping function for the specified website
    application.add_handler(sitescrapefunction)

    
    application.run_polling()
