---
id: bd2f5154-3a9f-4742-b94a-e5ef427defea
name: aws ec2 attach internet gateway to vpc
type: command
executor: bash
data: 'aws ec2 attach-internet-gateway --internet-gateway-id $AWS_INTERNET_GATEWAY_ID
  --vpc-id $AWS_VPC_ID --region $AWS_REGION

  '
output: null
created_at: '2020-07-31T04:25:29.802857+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws ec2 attach internet gateway to vpc

```bash
aws ec2 attach-internet-gateway --internet-gateway-id $AWS_INTERNET_GATEWAY_ID --vpc-id $AWS_VPC_ID --region $AWS_REGION

```
