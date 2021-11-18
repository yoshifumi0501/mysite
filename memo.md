# memo

1. 事前にクロームドライバーをダウンロードする
https://chromedriver.chromium.org/downloads

2. pipで関連のライブラリをいれる
https://qiita.com/hanzawak/items/2ab4d2a333d6be6ac760
https://qiita.com/mtskhs/items/edf7dbba9b0b0246ef8f

3. 変数指定する
- urlにクローリングしたいURLを。
例：url = "https://www.google.co.jp/"

- ミスったときのリトライ回数を指定する
例：retries_count = 5

- クロームドライバーのパスを指定する
例：executable_path = "/hogehoge/user/project//chromedriver"

3. 関数実行する
例: crawling(url, retries_count, executable_path)

4. とってきたhtmlデータをbeautiful soupで解析する（結構大変です）