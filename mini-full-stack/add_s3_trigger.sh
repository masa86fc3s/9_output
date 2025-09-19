#!/bin/bash
set -e  # エラー発生時にスクリプトを即終了させる

# -----------------------------
# 設定
# -----------------------------
STACK_NAME="mini-full-stack"   # CloudFormation スタック名
REGION="ap-southeast-2"       # AWS リージョン

# -----------------------------
# CloudFormation から出力値を取得
# -----------------------------
echo "🔍 CloudFormation 出力値を取得中..."

# CloudFormation スタックの出力から S3 バケット名を取得
BUCKET_NAME=$(aws cloudformation describe-stacks \
    --stack-name $STACK_NAME \
    --region $REGION \
    --query "Stacks[0].Outputs[?OutputKey=='InputBucketName'].OutputValue" \
    --output text)

# CloudFormation スタックの出力から Lambda 関数名を取得
LAMBDA_NAME=$(aws cloudformation describe-stacks \
    --stack-name $STACK_NAME \
    --region $REGION \
    --query "Stacks[0].Outputs[?OutputKey=='LambdaFunction'].OutputValue" \
    --output text)

# 確認表示
echo "✅ InputBucket: $BUCKET_NAME"
echo "✅ LambdaFunction: $LAMBDA_NAME"

# -----------------------------
# Lambda ARN を取得
# -----------------------------
# Lambda の詳細情報から ARN を取得
LAMBDA_ARN=$(aws lambda get-function \
    --function-name "$LAMBDA_NAME" \
    --region $REGION \
    --query 'Configuration.FunctionArn' \
    --output text)

# 確認表示
echo "✅ Lambda ARN: $LAMBDA_ARN"

# -----------------------------
# Lambda に S3 呼び出し権限を付与
# -----------------------------
echo "🔧 Lambda に S3 呼び出し権限を付与..."

# Lambda 関数に S3 からの Invoke(lambdaを実行する権限) 権限を追加
# 同じ権限がすでにある場合はエラーを無視
aws lambda add-permission \
    --function-name "$LAMBDA_NAME" \
    --statement-id s3-invoke \
    --action "lambda:InvokeFunction" \
    --principal s3.amazonaws.com \
    --source-arn "arn:aws:s3:::$BUCKET_NAME" \
    --region $REGION || echo "⚠️ Permission already exists"

echo "✅ Lambda に S3 呼び出し権限を付与完了"

# -----------------------------
# S3 → Lambda 通知設定
# -----------------------------
echo "🔧 S3 → Lambda 通知設定を登録..."

# S3 バケットにオブジェクト作成時（.csv ファイル）のイベント通知を Lambda に送信する設定
# 呼び出す Lambda の ARN
# S3 オブジェクト作成時にトリガー、*は全ての作成イベント(Put,Post,Copy)を対象とする
# .csv ファイルのみ対象
aws s3api put-bucket-notification-configuration \
    --bucket "$BUCKET_NAME" \
    --region $REGION \
    --notification-configuration "{
        \"LambdaFunctionConfigurations\": [
            {
                \"LambdaFunctionArn\": \"$LAMBDA_ARN\",
                \"Events\": [\"s3:ObjectCreated:*\"],
                \"Filter\": {
                    \"Key\": {
                        \"FilterRules\": [
                            {\"Name\":\"suffix\",\"Value\":\".csv\"}
                        ]
                    }
                }
            }
        ]
    }"
