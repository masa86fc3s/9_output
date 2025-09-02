# Docker
* Dockerfile, docker image, docker container の違いを説明できる
* Pythonの公式docker imageを使ってcontainerを作成
* ubuntu環境下でdockerを立ち上げ、awsのec2などサービスと連携させること

---

- 以下Docker desctopを使用した場合
* Docker fileを作成した後、実行させたいパイソンスクリプトを作成して、
    * docker build -t python_docker .(現在のディレクトリを表している)
    * docker run python_docker python --version


- 以下ubuntuにDockerをダウンロードした場合
    * WSLを有効化する
    * ubuntuをインストール
    * ubuntu環境下でDocker Engineをインストール
- Docker Engineをインストール
    #### 1. パッケージ更新
    * sudo apt-get update

    #### 2. 必要なツールをインストール
    * sudo apt-get install -y ca-certificates curl gnupg lsb-release

    #### 3. Docker公式GPGキーを登録
    * sudo mkdir -p /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
    sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

    #### 4. Dockerリポジトリを追加
    * echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
    https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

    #### 5. Docker本体をインストール
    * sudo apt-get update
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

#### Dockerイメージ作成
docker build -t python-docker .

#### コンテナ起動
docker run --rm python-docker

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
