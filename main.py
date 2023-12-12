import time

from cfg import *
from antimat_func import antimat


@bot.message_handler(content_types=['text'])
def test_func(message):
    # если пользователь отправил первое сообщение, происходит его идентификация
    chat_id = message.chat.id
    user_id = message.from_user.id

    try:
        if int(time.time()) - users[user_id].first_message_time < antispam_timeout * 60:

            # если за определенный промежуток времени пользователь отправил большое количество сообщений, то его сообщение удаляется
            if users[user_id].messages_from_user >= antispam_messages_count:
                bot.send_message(chat_id=chat_id, text='Вы не можете отправлять сообщения!')
                bot.delete_message(chat_id=chat_id, message_id=message.message_id)
            else:
                users[user_id].messages_from_user += 1
                if antimat(message=message):
                    input_mat(message=message)
                    users[user_id].first_message_time = int(time.time())
                    users[user_id].messages_from_user += antispam_messages_count
                    bot.delete_message(chat_id=chat_id, message_id=message.message_id)
                else:
                    input_func(message=message)
        else:
            users[user_id].first_message_time = int(time.time())
            users[user_id].messages_from_user = 1
            if antimat(message=message):
                input_mat(message=message)
                users[user_id].first_message_time = int(time.time())
                users[user_id].messages_from_user += antispam_messages_count
                bot.delete_message(chat_id=chat_id, message_id=message.message_id)
            else:
                input_func(message=message)

    except:
        users[user_id] = User
        users[user_id].first_message_time = int(time.time())
        users[user_id].messages_from_user = 1
        if antimat(message=message):
            input_mat(message=message)
            users[user_id].first_message_time = int(time.time())
            users[user_id].messages_from_user += antispam_messages_count
            bot.delete_message(chat_id=chat_id, message_id=message.message_id)
        else:
            input_func(message=message)


@bot.message_handler(content_types=['photo', 'document', 'video', 'sticker', 'audio', 'voice'])
def no_text_filter(message):
    chat_id = message.chat.id
    user_id = message.from_user_id

    try:
        if int(time.time()) - users[user_id].first_message_time < antispam_timeout * 60:
            # если за определенный промежуток времени пользователь отправил большое количество сообщений, то его сообщение удаляется
            if users[user_id].messages_from_user >= antispam_messages_count:
                bot.send_message(chat_id=chat_id, text='Вы не можете отправлять сообщения!')
            else:
                users[user_id].messages_from_user += 1
                users[user_id].first_message_time = int(time.time())
                users[user_id].messages_from_user += antispam_messages_count
        else:
            users[user_id].first_message_time = int(time.time())
            users[user_id].messages_from_user = 1
            users[user_id].first_message_time = int(time.time())
            users[user_id].messages_from_user += antispam_messages_count

    except:
        users[user_id] = User
        users[user_id].first_message_time = int(time.time())
        users[user_id].messages_from_user = 1

    finally:
        bot.delete_message(chat_id=chat_id, message_id=message.message_id)


def input_func(message):
    pass


def input_mat(message):
    pass


if __name__ == '__main__':
    bot.infinity_polling()
