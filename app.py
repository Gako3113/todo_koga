from html.entities import html5
from threading import Timer
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os


app = Flask(__name__)
# データベースの設定(sqliteファイルのパスを指定)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.sqlite'
db = SQLAlchemy(app)


# Todoリストのモデルを定義(db.Modelクラスを継承する必要がある)
class Todo(db.Model):
    # テーブル名を設定(テーブル名はクラス名の複数形が一般的)
    __tablename__ = 'todo'
    # 作成するテーブルのカラムを定義
    # ID
    id = db.Column(db.Integer, primary_key=True)
    # コンテンツ
    content = db.Column(db.String(200), nullable=False)
    # 作成日
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    #期限
    due = db.Column(db.DateTime, nullable=False)


# ルートにアクセスされたらインデックページを開く
@app.route('/', methods=['POST', 'GET'])
def index(): #アクションの定義
    # POSTメソッドで要求されたら
    if request.method == 'POST':
        # コンテンツを取得
        task_content = request.form['content']
        #期限を取得
        due = request.form.get('due')

        due = datetime.strptime(due, '%Y-%m-%d')
        # 新しいタスクを作成
        new_task = Todo(content=task_content, due=due)

        

        try:
            # データベースに新しいタスクを登録しトップページにリダイレクト
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "フォームの送信中に問題が発生しました"
    # 要求がない場合は、タスクリストを日付順に並べて表示
    else:
        tasks = Todo.query.order_by(Todo.due).all()
        return render_template('index.html', tasks=tasks)




# 削除画面
@app.route('/delete/<int:id>') #<int:id>には数字が入るイメージ
def delete(id): #アクションの定義
    # 削除するタスクのIDを取得
    task_to_delete = Todo.query.get_or_404(id)

    try:
        # 削除対象のタスクをDBから削除しトップページにリダイレクト
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return '削除中に問題が発生しました'

# 編集画面
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def update(id): #アクションの定義
    # 編集するタスクのIDを取得
    task_to_edit = Todo.query.get_or_404(id)
    # POSTメソッドがきたら編集対象のIDのコンテンツを更新
    if request.method == 'POST':
        #コンテンツの編集
        task_to_edit.content = request.form['content']
        #期限の編集
        task_to_edit.due = datetime.strptime(request.form.get('due'),'%Y-%m-%d')

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "タスクの編集中に問題が発生しました"
    else:
        return render_template('edit.html', task=task_to_edit)


# 完了画面
@app.route('/complete/<int:id>')
def complete(id): #アクションの定義
    # 削除するタスクのIDを取得
    task_to_delete = Todo.query.get_or_404(id)

    try:
        # 削除対象のタスクをDBから削除しトップページにリダイレクト
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return '完了中に問題が発生しました'





if __name__ == "__main__":
    app.run(debug=True)