## samファイルの構成

* sam build --template-file ec2-ssm-sam.yaml
    * 実行すると.aws-sam/build/ というディレクトリを自動生成します

* 初回のデプロイ時のみ　--guidedをつけてデプロイすれば以下の入力画面が表示され、それに順に答えていくとtomlファイルが自動で生成され、一度登録すればsam deployのみで実行できるようになる。
    * sam deploy --guided \
        --template-file ec2-ssm-sam.yaml
    * nsmna@□□□□□^□□ MINGW64 /c/rakus/スペックシート1/9_output/ec2-ssm/sam (master)
$ sam deploy --guided \
  --template-file ec2-ssm-sam.yaml

Configuring SAM deploy
======================

        Looking for config file [samconfig.toml] :  Not found

        Setting default arguments for 'sam deploy'
        =========================================
        Stack Name [sam-app]:
        AWS Region [ap-southeast-2]: 
        Parameter InstanceType [t2.micro]: 
        #Shows you resources changes to be deployed and require a 'Y' to initiate deploy
        Confirm changes before deploy [y/N]:
        #SAM needs permission to be able to create roles to connect to the resources in your template
        Allow SAM CLI IAM role creation [Y/n]:
        #Preserves the state of previously provisioned resources when an operation fails
        Disable rollback [y/N]:
        Save arguments to configuration file [Y/n]: 
        SAM configuration file [samconfig.toml]: 
        SAM configuration environment [default]: 

        Looking for resources needed for deployment:

        Managed S3 bucket: aws-sam-cli-managed-default-samclisourcebucket-wi2gdnuk469n
        Auto resolution of buckets can be turned off by setting resolve_s3=False
        To use a specific S3 bucket, set --s3-bucket=<bucket_name>
        Above settings can be stored in samconfig.toml

        Saved arguments to config file
        Running 'sam deploy' for future deployments will use the parameters saved above.
        The above parameters can be changed by modifying samconfig.toml
        Learn more about samconfig.toml syntax at
        https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-config.html

という質問事項が来るのでこれに回答していくと自動的にtomlファイルが作成される。


