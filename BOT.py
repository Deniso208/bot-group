import telebot
import http.client
import random
import time
starttime=time.time()

Token="1848358920:AAFRs2eh0G3xW01ywFDvVR4F9sVY-HtvBCI"
bot = telebot.TeleBot(Token)
random.seed()

foo = ['vladi_sap', 'tolya_harbych', 'Zargo_0', 'driveburn', 'pycikkk', 'ded_vnutr1', 'Archimareto', 'LloidFord', 'Andrei', 'nnnassstiia', 'Ḁ̣d͇̩a̶̪ ̠͡ ̭f̯̭ ̯͘ ͔̝rẹ͉i̥͝o̴͉ ҉̲̱', 'DimaGIad', 'Машка🐈‍⬛', 'Bishopchick', ' kap234', 'Sunnypiase', 'u1ser0001234']
data = []
@bot.message_handler(commands=['startt'])
def startt_message(message):
    bot.send_message(message.chat.id, "Список команд:\n/andreybulling\n/rusikbulling\n/danyabulling\n/dedbulling\n/artembulling\n/sapiehinbulling\n/pisun")
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
    bot.send_message(message.chat.id, + foo)

def timus(message):
    if True:
        spis = (random.choice(foo))
        bot.send_message(message.chat.id,'Абабо дня це- ' '@' + spis + '')
    elif  False:
        bot.send_message(message.chat.id, 'Упс я шось заЄбався')
        time.sleep(10)

@bot.message_handler(commands=['pisun'])
def pisun(message):
    pon = random.randint(0, 42)
    bot.send_message(message.chat.id, 'Пісюн ' + message.chat.username + ' - '+ str(pon) + 'CМ')
    # data.append(str(msg))
    # bot.register_next_step_handler(msg, start_message, data)


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
