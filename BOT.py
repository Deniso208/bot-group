import telebot
import http.client
import random
import time
starttime=time.time()
#5101327646:AAFmBDGfsnApng2Kfu21PEVNIvgTSUb9Bjo
#1848358920:AAFRs2eh0G3xW01ywFDvVR4F9sVY-HtvBCI
Token="1848358920:AAFRs2eh0G3xW01ywFDvVR4F9sVY-HtvBCI"
bot = telebot.TeleBot(Token)
random.seed()

foo = ['vladi_sap', 'tolya_harbych', 'Zargo_0', 'driveburn', 'pycikkk', 'ded_vnutr1', 'Archimareto', 'LloidFord', 'Andrei', 'nnnassstiia', 'Ḁ̣d͇̩a̶̪ ̠͡ ̭f̯̭ ̯͘ ͔̝rẹ͉i̥͝o̴͉ ҉̲̱', 'DimaGIad', 'Машка🐈‍⬛', 'Bishopchick', 'kap234', 'Sunnypiase', 'u1ser0001234', 'bokunoandi']
foo.sort()
data = []
@bot.message_handler(commands=['startt'])
def startt_message(message):
    bot.send_message(message.chat.id, "Список команд:\n/andreybulling\n/rusikbulling\n/danyabulling\n/dedbulling\n/artembulling\n/sapiehinbulling\n/pepsibulling")
@bot.message_handler(commands=['andreybulling'])
def Andrey_Bulling(message):
    chatId=message.chat.id
    bot.send_message(message.chat.id, "@bokunoandi , соси кок")
    bot.send_audio(message.chat.id, open("Соси.ogg", "rb"))
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEC2H1hMeilIE0dQwoMTFpLnyeY0UB2FgACHwEAAjFnwjWRtaMdS7iIaCAE")

@bot.message_handler(commands=['dedbulling'])
def Andrey_Bulling(message):
    chatId=message.chat.id
    bot.send_message(message.chat.id, "@ded_vnutr1 , соси кок")
    bot.send_audio(message.chat.id, open("бомбом.ogg", "rb"))
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEC2H1hMeilIE0dQwoMTFpLnyeY0UB2FgACHwEAAjFnwjWRtaMdS7iIaCAE")

@bot.message_handler(commands=['artembulling'])
def Andrey_Bulling(message):
    chatId=message.chat.id
    bot.send_message(message.chat.id, "@Archimareto , соси big black dick super puper plus ultra HD+ 4K")
    bot.send_audio(message.chat.id, open("Artem.ogg", "rb"))
    photo = open('артем.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['sapiehinbulling'])
def Andrey_Bulling(message):
    chatId=message.chat.id
    bot.send_message(message.chat.id, "@vladi_sap , Слава Уьтраправому")
    bot.send_audio(message.chat.id, open("reix.ogg", "rb"))
    photo = open('sap.png', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(commands=['music'])
def Music_Bulling(message):
    rand=random.randint(1,3)
    if (rand==1):
        bot.send_audio(message.chat.id, open("Муз1.ogg", "rb"))
    elif(rand==2):
        bot.send_audio(message.chat.id, open("Муз2.ogg", "rb"))
    elif(rand==3):
        bot.send_audio(message.chat.id, open("Муз3.ogg", "rb"))

@bot.message_handler(commands=['rusikbulling'])
def Rusik_Bulling(message):
    bot.send_message(message.chat.id, "Русик, сука, иди нахуй")
    rand=random.randint(1,9)
    if (rand==1):
        bot.send_audio(message.chat.id, open("Русик1.ogg", "rb"))
    elif(rand==2):
        bot.send_audio(message.chat.id, open("Русик2.ogg", "rb"))
    elif(rand==3):
        bot.send_audio(message.chat.id, open("Русик3.ogg", "rb"))
    elif(rand==4):
        bot.send_audio(message.chat.id, open("Русик4.ogg", "rb"))
    elif(rand==5):
        bot.send_audio(message.chat.id, open("Русик5.ogg", "rb"))
    elif(rand==6):
        bot.send_audio(message.chat.id, open("Русик6.ogg", "rb"))
    elif(rand==7):
        bot.send_audio(message.chat.id, open("Русик7.ogg", "rb"))
    elif(rand==8):
        bot.send_audio(message.chat.id, open("Русик8.ogg", "rb"))
    elif(rand==9):
        bot.send_audio(message.chat.id, open("Русик9(0).ogg", "rb"))
        bot.send_audio(message.chat.id, open("Русик9.ogg", "rb"))
    print(rand)

@bot.message_handler(commands=['joebulling'])
def Joe_Bidon(message):
    bot.send_message(message.chat.id, "Джо Байден")

@bot.message_handler(commands=['karmanbulling'])
def Karman_Bulling(message):
    bot.send_message(message.chat.id, "Поносус")
    bot.send_audio(message.chat.id, open("KARMANUS.ogg", "rb"))
    photo = open('SUS.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['danyabulling'])
def repeat_all_messages(message):
    #bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEClTZg8Ff8chF9AAHB_5ny-48k20OkoKgAAkAOAAIywglK38fhvyayJ3ogBA")
    video = open('Danya.mp4', 'rb')
    bot.send_video(message.chat.id, video)

@bot.message_handler(commands=['pepsibulling'])
def Peppsi_Bulling(message):
    rand=random.randint(1,2)
    if (rand==1):
        bot.send_audio(message.chat.id, open("pepsi1.ogg", "rb"))
        photo = open('pep.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif(rand==2):
        bot.send_audio(message.chat.id, open("pepsi2.ogg", "rb"))
        photo = open('pep2.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)


@bot.message_handler(commands=['links'])
def Links(message):
    bot.send_message(message.chat.id, "Ссылка на лекции, практику и тех способы передачи информации: \n/links_lection\n/Ссылка на менеджмент и аналитику R: \n/links_managment\n Ссылка стат методы: \n/links_methods\nСсылка на технику и технологию АПК: \n/links_agroHuita")

@bot.message_handler(commands=['links_lection'])
def Links_Lection(message):
    bot.send_message(message.chat.id, "meet.google.com/qnw-sumn-viy")

@bot.message_handler(commands=['links_managment'])
def Links_managment(message):
    bot.send_message(message.chat.id, "meet.google.com/txf-advs-jzx")

@bot.message_handler(commands=['links_methods'])
def Links_methods(message):
    bot.send_message(message.chat.id, "meet.google.com/pwv-vtgq-fxa")

@bot.message_handler(commands=['links_agroHuita'])
def Links_FIZRA(message):
    bot.send_message(message.chat.id, "meet.google.com/kyj-gxev-mrz")

@bot.message_handler(commands=['links_Practic'])
def Links_Practic(message):
    bot.send_message(message.chat.id, "https://meet.google.com/aou-hbsw-zzs")

@bot.message_handler(commands=['lessons'])
def Lessons_list(message):
    photo = open('lessons.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['list'])
def Abebrus_list(message):
    photo = open('list.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)

    
@bot.message_handler(commands=['all'])
def ALL(message):
    for x in foo:
        print('@' + x[0:17])
        bot.send_message(message.chat.id,'@' + x[0:17])


@bot.message_handler(commands=['aboba'])
def timus(message):
    if True:
        spis = (random.choice(foo))
        bot.send_message(message.chat.id,'Абабо дня це- ' '@' + spis + '')
    elif  False:
        bot.send_message(message.chat.id, 'Упс я шось заЄбався')
        time.sleep(10)

@bot.message_handler(commands=['pisun'])
def pisun(message):
    x=1
    intr=[0<x<42]
    pon = random.choice(intr)
    user = message.chat.username
    bot.send_message(message.chat.id, 'Пісюн ' + str(user) + ' - '+ str(random.randint(0,42))  + 'CМ')  

    
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Перекличка':
        for x in foo:
            bot.send_message(message.chat.id,'@' + x[0:])
    elif message.text.strip() == 'перекличка':
        for x in foo:
            bot.send_message(message.chat.id,'@' + x[0:])
    elif message.text.strip() == 'Сука':
        bot.send_message(message.chat.id,'Не лайся або подзвоню твоїй мамці малий ти засранець')
    elif message.text.strip() == 'cука':
        bot.send_message(message.chat.id,'Не лайся або подзвоню твоїй мамці малий ти засранець')
    elif message.text.strip() == 'Чорт':
        spis = (random.choice(foo))
        bot.send_message(message.chat.id,'Чорт дня це- ' '@' + spis + '')





# def start_message(message):
#     bot.send_message(message.chat.id, 'Ваш текст: ')




@bot.message_handler(commands=['top_pisun'])
def time(message):
    name = message.chat.username
    file=open('pis.txt','r')
    text=file.read()
    for i in text:
        i = name.index(i)
        print(text)




    # if name in text:
    #     bot.send_message(message.chat.id,  'True')
    # elif name != text:
    #     bot.send_message(message.chat.id,  'ГГ')

    



if __name__ == '__main__':
    bot.polling(none_stop=True)
