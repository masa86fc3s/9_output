# Linux
* 基本CLI操作であることを理解する
    * ls, cd, cp, mv, rm
* オプションの付け方について
    * ls -a
        * ハイフン一つはその後にアルファベット一文字
    * docker run --rm
        * ハイフン二つはその他
* ファイル権限
* ssh接続   
    * Remote SSH でもアクセスできるようにする
    * WSLからEC2インスタンスにssh接続できるようにする

---

## 以下は知っておくと会話がスムーズかも
* 実行可能ファイル
    * shebangもできれば調べておく
* シェルスクリプト
    * なんぞやくらいは知っておく
* 環境変数 
    * export ~
    * env
    * ターミナル切り替えると環境変数の設定はなくなる
        * .bashrc
            * ターミナル立ち上げたときに実行されるスクリプト



---

## Answer

- 1. オプションの書き方
    * ハイフン一つの後にアルファベット1文字
    * 長いオプションの場合
        * docker run --rm python-docker #コンテナ終了後に自動削除
        (長いオプションは意味が分かりやすく、複数文字をまとめて書ける)

- 2. ファイル権限
    * 権限の確認
        * ls -l
    * -rw-r--r--
        │ │ │ │ │
        │ │ │ │ └── othersの権限
        │ │ │ └── groupの権限
        │ │ └── userの権限
        │ └── ファイルタイプ (-:ファイル, d:ディレクトリ)
        └── specialフラグ（スキップしてOK）

        * r →読み取り
        * w →書き込み
        * x →実行
        * u →所有者
    * 権限付与
        * chmod u+x　ファイル名 (ユーザーに実行権限を追加)
        * chmod g-w　ファイル名 (グループから書き込み権限を削除)

## remote SSH接続
* 秘密鍵の準備
    * ec2作成時にダウンロードした.pemファイルを安全な場所に移動
    * chmod 600 ~/.ssh/my-key.pem
    * configファイルを作成（code ~/.ssh/config）
    * 設定などを記載する
    Host my-ec2
  HostName ec2-13-211-130-233.ap-southeast-2.compute.amazonaws.com
  User ubuntu          # Ubuntuの場合
  IdentityFile ~/.ssh/ssh_port.pem 
    * vscodeからの接続
        * vscode左下の><アイコンをクリック
        * remote-SSH
        * my-ec2を選択

---
## wslからssh接続
（序盤は一緒）
* 秘密鍵の準備
    * ec2作成時にダウンロードした.pemファイルを安全な場所に移動
    (このファイルをローカルではなく、作成したubuntu環境下のディレクトリに移動させるとこを勘違いしないように)
    * chmod 600 ~/.ssh/my-key.pem
    * configファイルを作成（code ~/.ssh/config）
    * 設定などを記載する
    * wslに入りまして、
        * ec2接続ページにあるssh -i から始まるやつを入力するとインスタンス起動
        * もしくはconfigで一度作成したら次回以降はssh my-ec2と入力するだけでインスタンスが立ち上がるようになる