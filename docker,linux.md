# Docker
* Dockerfile, docker image, docker container の違いを説明できる
* Pythonの公式docker imageを使ってcontainerを作成

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