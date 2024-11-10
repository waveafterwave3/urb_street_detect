##(@XAXAT0nBot) - tgbot
import spacy
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

model_path = "ner_model3" 
nlp = spacy.load(model_path)

async def analyze_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    doc = nlp(text)  
    response = "Адрес:\n"
    
    if doc.ents:
        for ent in doc.ents:
            response += f" {ent.text}"
    else:
        response = "Не удалось распознать адрес в тексте."


    await update.message.reply_text(response)

def main() -> None:

    TOKEN = "7510030771:AAGXFhvIdoXC9If5AJsobJd8uDfNwS_LKCI"


    application = Application.builder().token(TOKEN).build()




    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, analyze_message))


    application.run_polling()

if __name__ == "__main__":
    main()
