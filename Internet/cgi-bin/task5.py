## Обработка форм
# Создайте простую форму с заголовком «Авторизация», полями «Логин» и «Пароль» и кнопкой «Войти».
# Примите данные из формы, и если логин был «Admin», а пароль «123», то вместо формы вывести заголовок: «Здравствуйте, Admin!».
# Если логин и/или пароль введены другие, то сразу под заголовком у формы написать: «Неверные логин и/или пароль».
#!/usr/bin/python3
import cgi, html
r = cgi.FieldStorage()

message = ""
display = ""

log = html.escape(r.getvalue("log", ""))
pas = html.escape(r.getvalue("pas", ""))

if log != "Admin" and log != "":
    message = "<p style='color: red;'>Неверные логин и/или пароль!</p>"
elif log == "Admin" and pas == "123":
    display = "<p style='color: red;'>Здравствуйте, Admin!</p>"

print('Content-type: text/html; charset=utf-8')
print()
print("<html><head><title>Заголовок</title></head><body style='text-align: center;'>")

print('''
<form name="form" style="margin: 0 auto;" action="/cgi-bin/index2.py" method="post">
    <h2>Авторизация</h2>
    ''' + message +
    '''
    <label>Логин:</label>
    <input type="text" name="log" value="''' + log + '''" />
    <br />
    <br />
    <label>Пароль:</label>
    <input type="text" name="pas" value="''' + pas + '''" />
    <br />
    <br />
    <input type="submit" value="Войти" />
    ''' + display +
    '''</form>''')
print("</body></html>")
