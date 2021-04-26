from flask import Flask, render_template, request
import sqlite3
import os
import hashlib
import sqlite3

IMG_FOLDER = os.path.join('static', 'img')

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = IMG_FOLDER

autlog = False
name = ""


@app.route('/')
@app.route('/index')
def index():
    if autlog:
        return render_template('index_autlog.html', title='Солнечная система', name=name)
    else:
        return render_template('index.html', title='Солнечная система')


@app.route('/reg', methods=['POST', 'GET'])
def reg():
    return render_template("reg.html", error="")


@app.route('/reg_run', methods=['POST', 'GET'])
def reg_run():
    data = request.form

    pas1 = hashlib.md5(data["pass"].encode()).hexdigest()
    pas2 = hashlib.md5(data["pass_again"].encode()).hexdigest()

    if pas1 == pas2:
        if "@" in data["email"]:
            con = sqlite3.connect("db/Пользователи.db")
            cur = con.cursor()
            rezult = cur.execute('''SELECT * FROM Пользователи WHERE Email LIKE ?''', (data["email"],))
            rows = cur.fetchall()
            if len(rows) == 0:
                con = sqlite3.connect("db/Пользователи.db")
                cur = con.cursor()
                sql = '''INSERT INTO Пользователи(Имя, Email, Пароль) VALUES(?, ?, ?) '''
                rezult = cur.execute(sql, (data["name"], data["email"], pas1))
                con.commit()
                global autlog, name
                autlog = True
                name = data["name"]
                return render_template("succes.html", title="Вы зарегистрированы",
                                       text="Вы успешно зарегистрировались!")
            else:
                render_template("reg.html", error="Такой e-mail уже зарегистрирован")

        else:
            return render_template("reg.html", error="Некорректный e-mail")
    else:
        return render_template("reg.html", error="Пароли не совпадают")


@app.route('/log')
def log():
    return render_template("log.html")


@app.route('/log_run', methods=['POST', 'GET'])
def log_run():
    data = request.form

    if "@" in data["email"]:
        print(data)
        con = sqlite3.connect("db/Пользователи.db")
        cur = con.cursor()
        rezult = cur.execute('''SELECT * FROM Пользователи WHERE Email LIKE ?''', (data["email"],))
        rows = cur.fetchall()
        if len(rows) != 0:
            pas1 = rows[0][3]
            pas2 = hashlib.md5(data["pass"].encode()).hexdigest()
            if pas1 == pas2:
                global autlog, name
                autlog = True
                name = rows[0][1]
                return render_template("succes.html", title="Вы авторизованы", text="Вы успешно авторизовались!")
            else:
                return render_template("log.html", error="Неверный пароль")
        else:
            return render_template("log.html", error="Аккаунт с такой электронной почтой не найден")
    else:
        return render_template("log.html", error="Некорректный e-mail")


@app.route('/exit')
def exit():
    global autlog, name
    autlog = False
    name = ""
    return render_template("succes.html", title="Вы вышли", text="Вы вышли со своего аккаунта")


@app.route('/res')
def res():
    return render_template("res.html")


@app.route('/res_run', methods=['POST', 'GET'])
def res_run():
    data = request.form

    if "@" in data["email"]:
        print(data)
        con = sqlite3.connect("db/Пользователи.db")
        cur = con.cursor()
        rezult = cur.execute('''SELECT * FROM Пользователи WHERE Email LIKE ?''', (data["email"],))
        rows = cur.fetchall()
        if len(rows) != 0:
            pas1 = hashlib.md5(data["pass"].encode()).hexdigest()
            pas2 = hashlib.md5(data["pass_again"].encode()).hexdigest()
            if pas1 == pas2:
                rezult = cur.execute('''UPDATE Пользователи SET Пароль = ? WHERE Email LIKE ?''',
                                     (pas1, data["email"],))
                con.commit()
                global autlog, name
                autlog = True
                name = rows[0][1]
                return render_template("succes.html", title="Вы поменяли пароль", text="Вы успешно поменяли пароль!")
            else:
                return render_template("res.html", error="Пароли не совпадают")
        else:
            return render_template("res.html", error="Аккаунт с такой электронной почтой не найден")
    else:
        return render_template("res.html", error="Некорректный e-mail")


@app.route('/neptune')
def neptune():
    con = sqlite3.connect("db/Солнечная система.db")
    cur = con.cursor()
    rezult = cur.execute('''SELECT * FROM Объекты WHERE ID LIKE ?''', (1,))
    rows = cur.fetchall()
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'neptune.jpg')
    return render_template('page.html', img=full_filename,
                           title=rows[0][1], object=rows[0][1], info=rows[0][2], radius=rows[0][3],
                           volume=rows[0][4], distance=rows[0][5], temperature=rows[0][6])


@app.route('/uranus')
def uranus():
    con = sqlite3.connect("db/Солнечная система.db")
    cur = con.cursor()
    rezult = cur.execute('''SELECT * FROM Объекты WHERE ID LIKE ?''', (2,))
    rows = cur.fetchall()
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'uranus.jpg')
    return render_template('page.html', img=full_filename,
                           title=rows[0][1], object=rows[0][1], info=rows[0][2], radius=rows[0][3],
                           volume=rows[0][4], distance=rows[0][5], temperature=rows[0][6])


@app.route('/saturn')
def saturn():
    con = sqlite3.connect("db/Солнечная система.db")
    cur = con.cursor()
    rezult = cur.execute('''SELECT * FROM Объекты WHERE ID LIKE ?''', (3,))
    rows = cur.fetchall()
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'saturn.jpg')
    return render_template('page.html', img=full_filename,
                           title=rows[0][1], object=rows[0][1], info=rows[0][2], radius=rows[0][3],
                           volume=rows[0][4], distance=rows[0][5], temperature=rows[0][6])


@app.route('/jupiter')
def jupiter():
    con = sqlite3.connect("db/Солнечная система.db")
    cur = con.cursor()
    rezult = cur.execute('''SELECT * FROM Объекты WHERE ID LIKE ?''', (4,))
    rows = cur.fetchall()
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'jupiter.jpg')
    return render_template('page.html', img=full_filename,
                           title=rows[0][1], object=rows[0][1], info=rows[0][2], radius=rows[0][3],
                           volume=rows[0][4], distance=rows[0][5], temperature=rows[0][6])


@app.route('/mars')
def mars():
    con = sqlite3.connect("db/Солнечная система.db")
    cur = con.cursor()
    rezult = cur.execute('''SELECT * FROM Объекты WHERE ID LIKE ?''', (5,))
    rows = cur.fetchall()
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'mars.jpg')
    return render_template('page.html', img=full_filename,
                           title=rows[0][1], object=rows[0][1], info=rows[0][2], radius=rows[0][3],
                           volume=rows[0][4], distance=rows[0][5], temperature=rows[0][6])


@app.route('/earth')
def earth():
    con = sqlite3.connect("db/Солнечная система.db")
    cur = con.cursor()
    rezult = cur.execute('''SELECT * FROM Объекты WHERE ID LIKE ?''', (6,))
    rows = cur.fetchall()
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'earth.jpg')
    return render_template('page.html', img=full_filename,
                           title=rows[0][1], object=rows[0][1], info=rows[0][2], radius=rows[0][3],
                           volume=rows[0][4], distance=rows[0][5], temperature=rows[0][6])


@app.route('/venus')
def venus():
    con = sqlite3.connect("db/Солнечная система.db")
    cur = con.cursor()
    rezult = cur.execute('''SELECT * FROM Объекты WHERE ID LIKE ?''', (7,))
    rows = cur.fetchall()
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'venus.jpg')
    return render_template('page.html', img=full_filename,
                           title=rows[0][1], object=rows[0][1], info=rows[0][2], radius=rows[0][3],
                           volume=rows[0][4], distance=rows[0][5], temperature=rows[0][6])


@app.route('/mercury')
def mercury():
    con = sqlite3.connect("db/Солнечная система.db")
    cur = con.cursor()
    rezult = cur.execute('''SELECT * FROM Объекты WHERE ID LIKE ?''', (8,))
    rows = cur.fetchall()
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'mercury.jpg')
    return render_template('page.html', img=full_filename,
                           title=rows[0][1], object=rows[0][1], info=rows[0][2], radius=rows[0][3],
                           volume=rows[0][4], distance=rows[0][5], temperature=rows[0][6])


@app.route('/sun')
def sun():
    con = sqlite3.connect("db/Солнечная система.db")
    cur = con.cursor()
    rezult = cur.execute('''SELECT * FROM Объекты WHERE ID LIKE ?''', (9,))
    rows = cur.fetchall()
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'sun.jpg')
    return render_template('page.html', img=full_filename,
                           title=rows[0][1], object=rows[0][1], info=rows[0][2], radius=rows[0][3],
                           volume=rows[0][4], distance=rows[0][5], temperature=rows[0][6])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')