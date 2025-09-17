# GitHub Actions から SAM 自動デプロイまでの復習（完全版）

## 1️⃣ GitHub Actions の目的
- Push / PR などのトリガーで自動的に **SAM スタックをビルド＆デプロイ**
- 手作業で `sam build` や `sam deploy` を実行する必要がなくなる
- CI/CD の基本的な仕組みを体験できる

---

## 2️⃣ ディレクトリ構成とカレントディレクトリ
構成例：

```
9_output/
└─ mini-full-stack/
   ├─ template.yaml
   ├─ samconfig.toml
   └─ src/
      └─ app.py
└─ .github/workflows/
   └─ deploy.yml
```

- **template.yaml** と **samconfig.toml** は同じディレクトリに置く
- GitHub Actions では `working-directory: mini-full-stack` にするのがベスト

---

## 3️⃣ deploy.yml の基本構造

```yaml
name: Deploy SAM

on:
  push:
    branches: [ master ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Set up AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ap-southeast-2

      - name: Set up SAM CLI
        uses: aws-actions/setup-sam@v2

      - name: Build
        working-directory: mini-full-stack
        run: sam build

      - name: Deploy
        working-directory: mini-full-stack
        run: sam deploy --no-confirm-changeset
```

- `working-directory` を指定することで、`template.yaml` と `samconfig.toml` を正しく参照できる
- `samconfig.toml` があるので、`stack-name` や `S3 bucket` は自動で読み込まれる

---

## 4️⃣ SAM デプロイの仕組み
1. **`sam build`**
   - Lambda 関数のコードをパッケージ化
   - `CodeUri` に指定したディレクトリの内容をアーティファクトとして作成
2. **`sam deploy`**
   - CloudFormation スタックを作成/更新
   - `samconfig.toml` に保存された設定を自動適用
   - 必要に応じて S3 にアーティファクトをアップロード
   - SAM が Lambda 用ロールを自動生成（`Policies` に書いた権限だけ）

---

## 5️⃣ Lambda の IAM ロール自動作成
- `Policies` に書いた権限だけが自動で付与される
- 例：

```yaml
Policies:
  - S3ReadPolicy:
      BucketName: mini-full-stack
```

- SAM が Lambda 用のロール（例: `MyLambdaRole`）を自動作成
- Lambda はそのロールを使って実行される

### 注意点
- SAM が作るロールは **スタックに紐づく一時的なリソース名**  
- 権限のカスタマイズが必要な場合は手動で作成し、`Role: arn:aws:iam::...` を指定可能

---

## 6️⃣ トラブルシューティングまとめ

| 問題 | 原因 | 対処 |
|------|------|------|
| Template file not found | GitHub Actions のカレントディレクトリが違う | `working-directory` を指定する or パスを正しく書く |
| 循環依存 (Circular dependency) | Lambda / IAM / S3 が相互参照している | バケット名を固定、IAM ロールは SAM に自動作成させる |
| Lambda の CodeUri が見つからない | src/ ディレクトリや app.py が存在しない | `src/` とコードを正しく配置する |
| SAM CLI が権限エラー | ロールに権限がない | `Policies` を書いて SAM にロールを自動作成させる |
| S3 アップロード失敗 | S3 バケット未指定 | `samconfig.toml` にバケットを保存する or `--s3-bucket` 指定 |
| Python runtime エラー | Actions 上に Python 3.11 がない | `setup-sam@v2` が自動で対応するか、Docker コンテナでビルドする |

---

## 7️⃣ キモの理解ポイント
- `samconfig.toml` があると GitHub Actions では **コマンドをシンプルに書くだけで自動デプロイ可能**
- Lambda の IAM ロールは **Policies に書いた権限だけ** SAM が自動生成
- 循環依存を避けるために **動的バケット名は避ける**
- Lambda のコード (`app.py`) は GitHub Actions が自動でパッケージングするので、**Action 実行時に内容を差し替え可能**

---

## 8️⃣ 復習まとめ
- GitHub Actions で push すると自動でビルド・デプロイ
- `working-directory` と `samconfig.toml` が重要
- Lambda の IAM ロールは Policies に依存して自動作成
- 循環依存や S3 バケット指定ミスに注意
- 今回の流れを理解すると、次は **Glue / Athena / フルスタック統合** に進む準備が整う

