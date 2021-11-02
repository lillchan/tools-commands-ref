# aws
## logs
* [saw (logs)](https://github.com/TylerBrock/saw)

```bash
AWS_REGION=region AWS_PROFILE=profile saw watch loggroup
```

## s3
```bash
# download a file
aws s3 cp s3://bucketname/filename ./
```

## secrets
```bash
# create, get, and put base64 encoded
aws secretsmanager create-secret \
  --name secretname \
  --description 'description' \
  --secret-string 'secret' \
  --profile profile \
  --region region

aws secretsmanager get-secret-value
  --secret-id secretname \
  --query SecretBinary \
  --output text \
  --region region \
  --profile profile | base64 --decode

aws secretsmanager put-secret-value \
  --secret-id secretname \
  --secret-binary fileb://filename \
  --region region \
  --profile profile
```