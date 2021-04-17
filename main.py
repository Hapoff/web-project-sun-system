from flask import Flask, render_template
import sqlite3
import os

IMG_FOLDER = os.path.join('static', 'img')

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = IMG_FOLDER

autlog = True


@app.route('/')
@app.route('/index')
def index():
    if autlog:
        return render_template('index_autlog.html', title='Солнечная система')
    else:
        return render_template('index.html', title='Солнечная система')


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')