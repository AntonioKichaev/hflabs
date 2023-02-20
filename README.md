# hflabs
тестовое

В [базе знаний](https://confluence.hflabs.ru/pages/viewpage.action?pageId=1181220999) есть информация о кодах ответа нашего API.
Необходимо написать скрипт, который парсит эту табличку и переносит ее в гуглодоку. 
Предусмотреть, что в будущем необходимо будет синхронизировать данные в гуглодоке, 
если что-то изменится в базе знаний.
В результате нужно прислать:
- ссылку на код на гитхабе;
- ссылку на гуглодоку с перенесенной табличкой;
- информацию, сколько времени заняло выполнение задания.

Предпочтительный язык для выполнения задания — go. Допустимые языки — python, ruby.

## Plan
- Как спарсить таблицу, помню bs4 + pandas можно быстро спарсить
- Как создать гугл таблицу посмотреть api-шку
- Как сохранить padas в gdrive
- синхронизация документов подумать, обычно одностороненяя site->gdrive


## how to start
1. create venv
2. run terminal `pip install -r requirements.txt`
3. `client_secrets.json` - скачать кредлы  по инструкции [pyDrive2](https://docs.iterative.ai/PyDrive2/quickstart/)
4. `pg_id_parse` - страница в конфе которую хотим спарсить
5. `gdrive_excel_link` - куда положить файл
6. run main.py
7. мой gdrive [excel gdrive](https://docs.google.com/spreadsheets/d/1kZ5E7zE316kadIiKAWQE-o_xgagw5m5Ku45cDbWyzLI/edit#gid=1915296956)  

