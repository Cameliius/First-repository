import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from course import get_course

token = 'vk1.a.EUXNxhXrRnDAAn2p7rIVdqv8IVdyJxFarxAZpwbaqYfXOBKkUTZOBGge0dRf9ZHmIbKQEmuHtdLQAHuOKUZnXMY2-HuFzs6IQA9sD8eP2CddMtzxKqK6OESd3rRf1ImFhDCyXKn9dFhnhOBV7AhcJezAZUYta8Q_uVC__K7s8Q6C28SemCKZzncQDOjvN_WI8gfsHXfY7Kng-xC0DUZzoA'

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        user_id = event.user_id
        message_id = event.message_id

        if msg == 'привет':
            vk.messages.send(user_id=user_id, random_id=message_id, message='Привет)')
        elif msg == 'курс':
            response = get_course('R01235') + 'рублей за 1 доллар'
            vk.messages.send(user_id=user_id, random_id=message_id, message=response)
        elif msg.startswith('-к'):
            response = get_course(msg.split()[1])
            vk.messages.send(user_id=user_id, random_id=message_id, message=response)
