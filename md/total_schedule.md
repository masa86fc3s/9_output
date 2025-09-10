# AWSキャッチアップロードマップ

## 参画前・初期キャッチアップロードマップ（S3/Lambda/DynamoDB + Informatica含む）

| 順位 | 項目 | 内容 | 目安期間 | ポイント |
|------|------|------|-----------|----------|
| 1 | **IaC 基礎** | CloudFormation / SAM テンプレートの構造理解<br>Parameters / Resources / Outputs / Policies の確認 | 1日 | 小さなスタックで作ってデプロイしてみる |
| 2 | **AWS S3 / Lambda / DynamoDB** | - S3バケット作成<br>- Lambda作成 & S3イベントトリガー<br>- DynamoDBテーブル作成 & Lambdaから書き込み | 1〜2日 | 「イベント駆動型処理」のPoCを作る |
| 3 | **SaaS → S3 → Lambda → DynamoDB フロー理解** | - APIからデータ取得<br>- S3アップロード<br>- Lambdaイベント処理<br>- DynamoDB登録 | 1日 | Lambdaコードサンプルで実際に試す |
| 4 | **IAMロール・権限** | - LambdaからS3/DynamoDBアクセス権限<br>- 最小権限原則の理解 | 半日 | PoCスタックで権限の付け方を確認 |
| 5 | **EC2 + SSM (参画初期用)** | - Session Manager経由で接続<br>- IAMロール付与、ポリシー確認 | 半日 | 実務での接続操作に慣れる |
| 6 | **Informatica（IICS）基礎** | - データ統合・ETLの概念<br>- On-Demandトレーニングで画面操作確認<br>- SaaS連携イメージ | 1〜2日 | S3/Lambdaフローとの類似点を意識 |
| 7 | **GitHub Actionsによる自動デプロイ（任意）** | - SAM/CloudFormationデプロイ自動化<br>- Lint / 単体テスト | 半日 | PoCスタックで試す |
| 8 | **Glue / Athena / フルスタック統合** | - 小スタック + VPC / EC2 / Glue / Athena統合<br>- IAMロール・権限整理 | 1〜2日 | PoC理解後に段階的に追加 |


## キャッチアップ進め方のポイント

1. **最初は小スタックPoCで手を動かす**
   - S3 + Lambda + DynamoDB
   - イベント駆動型処理の流れを体験
2. **並行してInformatica概念理解**
   - SaaS連携やETLフローを頭の中でイメージ
3. **IaCを通じてAWSリソース作成・権限管理に慣れる**
   - 小規模スタックでデプロイ → 更新 → 削除
4. **余力があればGitHub Actionsで自動化**
   - デプロイパイプラインの体験
5. **PoC理解後にフルスタック統合**
   - VPC、EC2、Glue、Athenaを順次追加


💡 このロードマップなら、参画前に **IaC・イベント駆動型処理・Informaticaの基礎** を押さえつつ、実務で必要になるAWSリソース操作の理解を効率的に進められます。

