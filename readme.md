# Что было сделано 
Скрипт реализует парсинг данных с сайта https://quotes.toscrape.com/.
### Полученные данные включают в себя:
- все цитаты с сайта
- авторы цитат и ссылки на них
- теги, соответствующие цитатам и ссылки на них

# Откуда были получены данные
Со всех веб-страниц сайта https://quotes.toscrape.com/

# Как осуществлялся сбор
Сбор осуществлялся при помощи библиотеки curl-cffi для отправки HTTP-запросов на сайт и получения текста веб-страницы
и библиотеки BeautifullSoup для парсинга HTML-разметки веб-страницы.
Сначала были получены все страницы сайта с их содержимым, потом непосредственно парсинг полученных данных с сохранением в файл в формате JSON.

# Почему был выбран тот или иной метод/инструмент, а не другой
Был выбран этот способ, потому что сервер выдавал уже сформированную HTML-страницу, а не данные в формате JSON, не использовались инструменты,
автоматизирующие и эмулирующие работу браузера, так как не было необходимости в них (никаких действий от пользователя на сайте не требовалось)