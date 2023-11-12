from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)

def init_db():
    with sqlite3.connect('database.db') as db: #database.db생성 
        c = db.cursor() #데이터베이스 연결을 통해 커서를 생성 
                        #커서는 SQL 명령을 실행하고 결과를 얻는데 사용
        c.execute('''   
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            );
        ''') # 커서를 사용해 SQL명령을 실행함

def add_user(username, password):   # 
    with sqlite3.connect('database.db') as db:
        c = db.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        db.commit()


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/loginsuccess')
def login_succes():
    return '로그인 성공'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect('database.db') as db:
            c = db.cursor()
            c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
            user = c.fetchone()
            if user is not None:
                return redirect(url_for('login_succes'))  # 로그인 성공
            else:
                return '로그인 실패'  # 로그인 실패
    return render_template('login.html')  # GET 요청이면 로그인 폼을 보여줌




if __name__ == '__main__':
    app.run(debug=True)