# 必要なスキル
    
* 詳細設計書の作成経験
* ETLツールでの設計・実装経験
* 課題に関する共有と自己解決力
* Amazon S3、AWS Lambda/Glue、Amazon Timestream、Amazon Athena使った設計・開発経験
* Python、SQLを使った設計・開発経験
* 新しい技術へのキャッチアップ意欲

# 業務内容
　１．Informatica Integration Cloud Service(CDI)(以降、IICS)ツールによる実装
      IICSにて詳細設計書から実装を行う。
      ETLした結果をGoogle Cloud BigQueryあるいはAmazon S3に配置する。

　２．AWS Lambdaによる実装
　　　IICSにて詳細設計書から実装を行う。
　　　SaaSからデータをAPIにて取得、AWSのS3に配置する。

　３．詳細設計書作成（バッチ(ETL)設計）
　　　基本設計から詳細設計書を作成する

　４．運用監視、構築済み機能のパフォーマンス改善
　　　IICSおよびAWS機能に対してのエラー監視及びエラー時の運用対応を行う。
　　　構築済みAWS機能（EC2・EBS等）に対してパフォーマンス等の改善活動を行う。

# これらを踏まえて
* お聞きしたいとこと
    * awsの連携はどの程度できていた方がいいですか
    * docker,linuxはどの程度使用しますか？
    * pythonとSQLのレベル感はどの程度ですか？
    * インフォマティカは触れておいた方が良いですか？（一応airflowは触ったことがあります）
    * 社内の雰囲気はどうですか？
    * 事前にキャッチアップしておいた方が良いことはありますか？
    
## 現状考えている想定
- wsl,ubuntu上でdockerコンテナを立ててそこでawsのサービスを使用していく。
- s3にあるデータをathenaを使ってSQL文で前処理を行い、lamdaで何かしらのトリガーを発生させて自動的に処理を加えて、インフォマティカに出力するようにしほうがいいのかな？
- EC2も使った方が良いですかね？

---

## 追記

顔合わせの際にお伝えした通り、事前準備は必要ないように弊社側で準備しています。
とは言え…な部分はあると思いますので、参画前に少しでも見ておくとスムーズだろうと考えられるものを三鴨セレクトでいくつか記載いたします。
1) Informatica について
案件説明時にスライドでお伝えしたものです。

弊社技術ブログ DevelopersIO の紹介記事
https://dev.classmethod.jp/articles/informatica-intelligent-cloud-services/
Informatica オンデマンドトレーニング
https://now.informatica.com/IICS-Cloud-Data-Integration-Services-onDemand-Japanese.html?loid=67804d32-b34c-4af0-b22e-46202ba70c87%20-

2) VPC プライベートサブネットにある EC2 インスタンスに Systems Manager Session Manager 経由で SSH アクセス
このやり方で EC2 に接続していただくことになるので、クライアント（業務端末）側のセットアップも含めて一度やっておくといいと思います。
EC2 はプロジェクトでは RHEL を使っていますが、Amazon Linux 2023 のような Linux OS であればなんでもいいと思います。

3) IaC
AWS リソースの管理のために IaC で AWS SAM / CloudFormation を利用しています。
どんなことができるのか、どんなコードになるのかを見ておくといいと思います。

4) DynamoDB
データを持つストレージ（データベース）というよりは設定値を管理するために使っています。
アクセスの方法やデータの持ち方が違うので、触って体験しておくといいと思います。
---
