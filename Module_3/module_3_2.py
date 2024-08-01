def send_mail(message, recipient, sender):
    b = ('.com', '.ru', '.net')
    if sender != recipient:
        if '@' in recipient:
            if '@' in sender:
                if recipient.endswith(b):
                    if sender.endswith(b):
                        if sender == 'university.help@gmail.com':
                            print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
                        else:
                            print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)
                    else:
                        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
                else:
                    print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
            else:
                print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
        else:
            print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    else:
        print('Невозможно отправить сообщение самому себе!')

send_mail('hallo',
          'university.help@gmail.com',
          sender='university.help@gmail.com')
