import telebot
import http.client
import random
import time
starttime=time.time()

Token="1848358920:AAFRs2eh0G3xW01ywFDvVR4F9sVY-HtvBCI"
bot = telebot.TeleBot(Token)
random.seed()

@bot.message_handler(commands=['startt'])
def startt_message(message):
    bot.send_message(message.chat.id, "Список команд:\n/andreybulling\n/rusikbulling\n/danyabulling\n/dedbulling\n/artembulling")
    if (message.text=="Рил"):
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEClTZg8Ff8chF9AAHB_5ny-48k20OkoKgAAkAOAAIywglK38fhvyayJ3ogBA")
    elif (message.text=="рил"):
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEClTZg8Ff8chF9AAHB_5ny-48k20OkoKgAAkAOAAIywglK38fhvyayJ3ogBA")

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

    
@bot.message_handler(commands=['all'])
def ALL(message):
    bot.send_message(message.chat.id, "Перекличка! @Zargo_0 , @Sunnypiase , @tolya_harbych, @u1ser0001234, @Archimareto @Машъка, @kap234, @ded_vnutr1, @pycikkk, @dderksenn, @Sakura77777777, @portubas, @bokunoandi, @Сладкий, @vladi_sap, @nnnassstiia")

#@bot.message_handler(commands=['test'])
#def Joe_Bidon(message):
#    bot.send_message(message.chat.id, "Тест")
#    bot.send_photo(message.chat.id, "https://dub01pap001files.storage.live.com/y4myk6raYmlun7_MIMUPpV59L_kGdYsIWhhsxpfHqorJVZdVZpUen_F1zC8L9GsGTpLX0IOwHYvz_cO21uDN-UhwcWny4drWgSOiw2oboERdwy43Zo61dB6slBM7UEQmAyv2xNiMvdw74_x-QGsBYpaXbr4R7cZc-xKJue6xK7mGYT6IF947i6LwFzg3lngcNmwOF23AuTQV9zlAjU1l-rCxkjCVhQvutxkhhiRkRAEi0I?encodeFailures=1&width=691&height=722")

#@bot.message_handler(commands=['testA'])
#def Joe_Bidan(message):
#    bot.send_message(message.chat.id, "Тест")
#    bot.send_document(message.chat.id, "https://drive.google.com/file/d/1M6uhghGids6jkrUnPXGaHrIrAxdPFTdc/view?usp=sharing")

 
if __name__ == '__main__':
     bot.polling(none_stop=True)