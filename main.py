from flask import Flask, render_template

app = Flask(__name__)

autlog = False


@app.route('/')
@app.route('/index')
def index():
    if autlog:
        return render_template('index_autlog.html', title='Солнечная система')
    else:
        return render_template('index.html', title='Солнечная система')


@app.route('/neptune')
def neptune():
    return "Страница планеты 'Нептун'"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')