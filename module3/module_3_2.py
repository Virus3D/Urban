def send_email(message, recipient, sender = "university.help@gmail.com"):
    check_recipient = '@' not in recipient or ('.com' not in recipient and '.ru' not in recipient and '.net' not in recipient)
    check_sender = '@' not in sender or ('.com' not in sender and '.ru' not in sender and '.net' not in sender)
    if check_recipient or check_sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return
    
    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        return
    
    print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')