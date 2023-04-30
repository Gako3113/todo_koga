# To do リスト

#### Description:

これは私が初めて開発したwebアプリケーションです。
私がCS50 ファイナルプロジェクトで作成したwebアプリケーション「To doリスト」はユーザーがタスクを管理し、
同時にストップウォッチでユーザーがタスクをこなす時間を測ることのできるタスク管理アプリケーションです。


### 使い方
トップページではユーザーにタスクの入力と締切日の入力を求められます。
タスクと締切日を記入すると、今登録されているタスクの情報が表示され、その下にはタスクを記入するフォームと、締め切り日の入力するフォームが残るようになっています。
ここでフォームに記入することで、何個でもタスクを記入することが出来ます。

データベーステーブルには、登録されているタスク内容、登録日である今日の日付、設定した締切日、アクションが表示され、
またその隣にストップウォッチが表示されるようになっています。

次にストップウオッチ機能について説明します。
スタートを押すとストップウォッチが開始し、ストップを押すと止めることが出来ます。
リセットを押すと履歴を消すこともできます。
ストップウォッチ機能は、最優先でやるべきタスクにのみ使用できるよう、提出期限の最も近いタスクにだけ使用することが出来ます。
ここには、ユーザーが時間を測ってタスクに集中し、締め切りに間に合わせることが出来るようにという私の思いが込めてあります。
また、他のタスクのストップウォッチ機能は締め切り日が近いタスクが終われば自動的に一番上に表示されるようになっており、一番上に表示されれば使えるようになります。

最後にアクションの3つのボタンについて説明します。
「やっぱやめる」のボタンを押すとタスクがデータベースから消去され、表示も消えます。
「終わったー」のボタンを押すとこれもまたタスクの表示が消去されます。
「ちょっと変える」のボタンを押すと、編集ページが表示され、タスクと締切日の変更が出来ます。


### 使った技術

#### - Python
#### - Flask
#### - HTML
#### - CSS
#### - JavaScript

