# Работа с cookie
# Доработайте предыдущее упражнение, чтобы, если пользователь уже успешно вошёл, то при обновлении страницы ему всегда писалось: 
    # «Здравствуйте, Admin!».
# Добавьте ссылку выхода, например, такую: «index.py?logout=1», которую обработайте так, чтобы cookie поменялись на пустые значения. 
    # Таким образом, после этого снова должна появиться форма входа.
# Сделайте так, чтобы ссылка выхода была только, если пользователь авторизован.
# Примечание: небезопасно хранить открытый пароль в cookie, поэтому как дополнительное задание, используя справочник, 
    # найдите функцию, которая будет хэшировать пароль (например, через алгоритм md5). Дальше храните в cookie уже хэшированный пароль, 
    # и сравнивать уже его надо будет не со строкой «123», а также с результатом хэширования этой строки.

#!/usr/bin/python3
import cgi, html, http.cookies, os
r = cgi.FieldStorage()

message = ""
display = ""

log = html.escape(r.getvalue("log", ""))
pas = html.escape(r.getvalue("pas", ""))

if log != "Admin" and log != "":
    message = "<p style='color: red;'>Неверные логин и/или пароль!</p>"
elif log == "Admin" and pas == "123":
    display = "<p style='color: red;'>Здравствуйте, Admin!</p>"
    print("Set-cookie: log=" + log)
    print("Set-cookie: pas=" + pas)

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
log = cookie.get("log").value
pas = cookie.get("pas").value


print('Content-type: text/html; charset=utf-8')
print()
print("<html><head><title>Заголовок</title></head><body style='text-align: center;'>")

print('''
<form name="form" style="margin: 0 auto;" action="/cgi-bin/index4.py" method="post">
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
    '''
    </form>''')
print("</body></html>")