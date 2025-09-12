# EC2 + SSM (Session Manager) 学習まとめ

## 1️⃣ 前提・目的
- **目的**：ローカルPCから AWS CLI を使って EC2 に安全に接続する
- **環境**：
  - OS: Windows + Git Bash (MINGW64)
  - AWS CLI インストール済み
  - EC2 インスタンス（SSM Agent稼働確認済み）
  - IAM ユーザー `masa86fc3s` に必要な権限を付与する準備

---

## 2️⃣ EC2の準備
1. EC2インスタンス作成（または既存インスタンス利用）
2. **IAMロール付与**：
   - `AmazonSSMManagedInstanceCore` を EC2 にアタッチ
3. **SSM Agent 稼働確認**
```bash
sudo systemctl status amazon-ssm-agent
```
- 「active (running)」で稼働確認

---

## 3️⃣ ローカル環境の準備
1. **AWS CLI で SSM接続** するには Session Manager Plugin が必要
2. **インストール**
   - [公式リンク](https://s3.amazonaws.com/session-manager-downloads/plugin/latest/windows/SessionManagerPluginSetup.exe) からダウンロード
   - 実行してインストール
3. **Git Bash で PATH 通す**
```bash
export PATH=$PATH:"/c/Program Files/Amazon/SessionManagerPlugin/bin"
```
- 永続化は `~/.bashrc` に追加

---

## 4️⃣ IAM ユーザー権限付与
- 最小権限ポリシー例：
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ssm:StartSession",
        "ssm:DescribeInstanceInformation",
        "ssm:GetConnectionStatus",
        "ssm:TerminateSession"
      ],
      "Resource": "*"
    }
  ]
}
```
- ユーザーにアタッチ
- CLIから `aws ssm start-session` が実行可能に

---

## 5️⃣ CLI接続確認
```bash
aws ssm start-session --target <インスタンスID>
```
- 接続後：
```bash
whoami
ls
exit
```
- ターミナル上で EC2 の操作が可能

---

## 6️⃣ ポイント・応用
- **インスタンスIDを変えるだけで他の EC2 も同様に接続可能**
- **ポートフォワード**や **スクリプト自動化** にも活用できる
```bash
aws ssm start-session --target <インスタンスID>   --document-name AWS-StartPortForwardingSession   --parameters '{"portNumber":["3306"],"localPortNumber":["3306"]}'
```
- 実務では CLI 接続が主流で、ブラウザ経由は補助的

---

💡 学習ポイント
- EC2 と IAM ロールの関係を理解
- SSM Agent の役割と稼働確認方法
- Session Manager Plugin のインストールと PATH 設定
- 最小権限ポリシー作成で CLI 接続可能にする方法
- Git Bash での CLI 接続手順
