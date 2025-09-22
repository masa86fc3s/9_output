## cloudformation接続
* まず前提
    * AWS CLI がインストール済み
    * 適切な IAM 権限（CloudFormation, EC2, IAM, SSM, SecurityGroup）を持つユーザー
    * リージョン：ap-southeast-2（シドニー）

* UTF-8になっていないとデプロ時にエラーになります
（スペース、ハイフン、全角が入っているとなりやすい、コメントも含め）

* デプロイ
$$
aws cloudformation deploy \
  --template-file ec2-ssm-cloudformation.yaml \
  --stack-name session-manager-ec2-cfn \
  --region ap-southeast-2 \
  --capabilities CAPABILITY_NAMED_IAM
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

