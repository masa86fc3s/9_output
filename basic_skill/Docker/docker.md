# Docker
* Dockerfile, docker image, docker container の違いを説明できる
* Pythonの公式docker imageを使ってcontainerを作成

- 以下Docker desctopを使用した場合
* Docker fileを作成した後、実行させたいパイソンスクリプトを作成して、
    * docker build -t python_docker .(現在のディレクトリを表している)
    * docker run python_docker python --version

- 以下ubuntuにDockerをダウンロードした場合

--- 

## ANSER

- Docker file (build)
    * Dcoker imageを作成するための設計図
        * どのOSを使うか
        * 必要なパッケージのインストール
- Docker image (run)
    * Docker fileを元にして作成した実体
    (Dcoker containerの動作環境についてまとめたファイル)
        * 読み取り専用で変更はできない
        * バージョンの指定が可能
        * どの環境でも動かすことができる
- Docker container
    * docker imageを元に実際に動いている実行環境
        * Docker imageをコピーして、書き込み可能なレイヤー(層)を追加した物
        * 実行中のアプリそのもの
        * このコンテナは独立した環境として存在し、他のコンテナやホストとなる環境に影響することはない

---

## 堀尾さんからのアドバイス
★9月のアウトプット

docker をcl
前処理自動化してみた！
足し算の自動化
足し算のプログラミングを
docker image 使って、デプロイしてみた！
自動化してみた。
pythonのパッケージ管理も同時にできるように
ポエトリー（依存関係を自動的に見てくれる）
pyenv
uv（インストールが早く終わる、最近のトレンド）パッケージ管理
ローカル環境には何もインストールせず、
docker内で完結させること
クラウドにデプロイするときはapi下しないといけない



1.docker imageの使用
2.パッケージ管理
3.awsとの接続

wslをubuntuを構築して
.docker構築　パイソン
1windows からlinuxでubuntuを構築する
2docker 構築　してパイソン
