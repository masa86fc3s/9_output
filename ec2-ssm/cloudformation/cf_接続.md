## cloudformation接続
* まず前提
    * AWS CLI がインストール済み
    * 適切な IAM 権限（CloudFormation, EC2, IAM, SSM, SecurityGroup）を持つユーザー
    * リージョン：ap-southeast-2（シドニー）

---

* 自身が今どのユーザーを使用しているのかは以下のコマンドで確認可能
  * aws sts get-caller-identity
* aws cliにiamユーザーを登録したいとき
  * aws configure --profile <IAMユーザー名>
  * この際にキーやリージョンといった情報が必要
* 現在登録しているユーザーの確認
  * aws configure list-profiles
* ユーザーを切り替えたいときは
  * aws sts get-caller-identity --profile <IAMユーザー名>

---

* UTF-8になっていないとデプロ時にエラーになります
（スペース、ハイフン、全角が入っているとなりやすい、コメントも含め）

* デプロイ
$$
aws cloudformation deploy \
  --template-file ec2-ssm-cloudformation.yaml \
  --stack-name session-manager-ec2-cfn \
  --region ap-southeast-2 \
  --capabilities CAPABILITY_NAMED_IAM \
  --profile ssm_cloud_formation       ←ここに登録したIAMユーザーを指定することで権限の振り分けも可能 
$$

* 削除したいとき
$$
aws cloudformation delete-stack \
  --stack-name session-manager-ec2-cfn \
  --region ap-southeast-2

$$

* 作成確認

$$
aws cloudformation describe-stacks \
  --stack-name session-manager-ec2-cfn \
  --region ap-southeast-2

$$

*  リージョンを変更するときにはそれに伴ったami idも必ず変更しなければならない
  * こうすることでssm接続が可能になる。
