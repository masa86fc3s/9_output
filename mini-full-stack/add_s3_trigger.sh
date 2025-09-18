#!/bin/bash
set -e

# -----------------------------
# 設定
# -----------------------------
STACK_NAME="mini-full-stack"
REGION="ap-southeast-2"

# -----------------------------
# CloudFormation から出力値を取得
# -----------------------------
echo "🔍 CloudFormation 出力値を取得中..."

BUCKET_NAME=$(aws cloudformation describe-stacks \
    --stack-name $STACK_NAME \
    --region $REGION \
    --query "Stacks[0].Outputs[?OutputKey=='InputBucketName'].OutputValue" \
    --output text)

LAMBDA_NAME=$(aws cloudformation describe-stacks \
    --stack-name $STACK_NAME \
    --region $REGION \
    --query "Stacks[0].Outputs[?OutputKey=='LambdaFunction'].OutputValue" \
    --output text)

echo "✅ InputBucket: $BUCKET_NAME"
echo "✅ LambdaFunction: $LAMBDA_NAME"

# -----------------------------
# Lambda ARN を取得
# -----------------------------
LAMBDA_ARN=$(aws lambda get-function \
    --function-name "$LAMBDA_NAME" \
    --region $REGION \
    --query 'Configuration.FunctionArn' \
    --output text)

echo "✅ Lambda ARN: $LAMBDA_ARN"

# -----------------------------
# Lambda に S3 呼び出し権限を付与
# -----------------------------
echo "🔧 Lambda に S3 呼び出し権限を付与..."

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

aws s3api put-bucket-notification-configuration \
    --bucket "$BUCKET_NAME" \
    --region $REGION \
    --notification-configuration "{
        \"LambdaFunctionConfigurations\": [
            {
                \"LambdaFunctionArn\": \"$LAMBDA_ARN\",
                \"Events\": [\"s3:ObjectCreated:*\"] ,
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

echo "✅ S3→Lambda トリガー設定が完了しました"
