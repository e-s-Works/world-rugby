## site:ワールドラグビーからランキングデータをスクレイピング【Python】【スクレイピング】

[Youtubeで動画を公開中](https://youtu.be/Va2S5cBCKJ8)

サイト　　　　：ワールドラグビー<br>
収集するデータ：2022年度の男子日本代表チームのランキングデータ<br>
アウトプット　：HTMLで表示

### プロジェクト構成
- main.py
- page.py
- locators.py
- output_template.html

### 開発環境
- Windows10
- Python 3.11.0
  - selenium 4.7.2
  - webdriver-manager  3.8.5

### 実行するアクション
- クリック
- 画面の表示位置の変更
- テーブル行の背景色を変更
- テキストの取得
- タブの作成
- アクティブなタブの切り替え
- HTMLをページに挿入
