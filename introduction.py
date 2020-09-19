import telebot
import config
bot = telebot.TeleBot(config.token)


def start(message):
    bot.send_message(message.chat.id, 'Приветствую) Я бот-админ для чата.\nСправку по'
                                      ' командам можно получить по команде /help@sanya_pilot_bot\nЕсли что-то не '
                                      'работает, пните @alexander_baransky496\n')


def help(message):
    bot.send_message(chat_id=message.chat.id,
                     text='Список команд:\n'
                          '/tr - Перевести сообщение. /tr <код языка, на который надо перевести>'
                          '/notes - Показать список заметок\n'
                          '/note - Просмотр заметки\n'
                          '/addnote - Добавить заметку\n'
                          '/delnote - Удалить заметку\n'
                          '/mute - Мут навсегда (до размута)\n'
                          '/tmute - Мут на время. Время прописывается в формате <кол-во><s/m/h/d>\n'
                          '/unmute - Размут\n'
                          '/ban - Забанить пользователя навсегда (до разбана)\n'
                          '/banme - Забанить пользователя, написавшего команду\n'
                          '/tban - Забанить пользователя на время. Формат такой же как в /tmute\n'
                          '/unban - Разбан\n'
                          '/kick - Кикнуть пользователя\n'
                          '/kickme - Кикнуть пользователя, написавшего команду\n'
                          '/restrict - Лишение пользователя всех прав\n'
                          '/permit - Выдача пользователю всех прав\n'
                          '/dpermit - Выдача пользователю дефолтных прав чата\n'
                          '/demote - Лишение пользователя всех административных прав (пока не работает)\n'
                          '/promote - Выдача пользователю всех административных прав (пока не работает)\n'
                          '/weather - Показать текущую погоду. /weather <название города>'
                          'Чтобы применить все эти команды, необходимо ответить командой на сообщение пользователя, '
                          'которого вы хотите кикнуть, забанить и т. д.')