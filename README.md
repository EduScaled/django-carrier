
# Описание

Django-приложение, обертка над пакетом (https://github.com/EduScaled/carrier-client), обеспечивающее коммуникацию между Carrier (https://github.com/EduScaled/carrier) и django-приложением

Используемый стек: ```python3.x```, ```django2.x```

# Установка

1. В вашем виртуальном окружении выполнить комманду ```pip install git+https://github.com/EduScaled/django-carrier-client``` 
2. Проверить, был ли ранее установлен пакет Carrier-package, при необходимости установить его 
```pip install git+https://github.com/EduScaled/carrier-client``` 

# Использование

Основные объекты, которые используются описаны в пакете https://github.com/EduScaled/carrier-client.
Способы отправки сообщения также описаны в документации к пакету и текущем варианты остаются неизменными.

Приложение добавляет callback url (см. ```urls.py```), который требуется подключить к основному приложению.

Также предоствлен механизм по регистрации обработчиков событий - ```MessageManagerHelper```.
Для активации механизма прослушивание в вашем django-приложении требуется:

Добавить в  ```__init__.py```

```
from carrier_client.manager import MessageManager
from django_carrier_client.helpers import MessageManagerHelper

# Менеджер, который будет слушать заданные топики у заданного приложения
to_listen = MessageManager(
    topics=["uploads"],
    host="185.12.29.14",
    port=80
)

# Регистрируем обработчик,  если should_handle возвращает True - значит к нему применить функцию handler

to_listen.register_event_handler(
    should_handle=lambda message: True,
    handler=lambda message: print(message.get_payload())
)

# Добавляем менеджер на прослушивание

MessageManagerHelper.set_manager_to_listen(to_listen)
```