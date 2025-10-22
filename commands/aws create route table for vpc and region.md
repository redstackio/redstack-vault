---
id: 2815d60d-de33-4949-abab-d63c903a49a7
name: aws create route table for vpc and region
type: command
executor: bash
data: 'aws ec2 create-route-table --vpc-id $AWS_VPC_ID --region $AWS_REGION

  '
output: aws ec2 create-route-table --vpc-id vpc-010123123 --region us-east-1
created_at: '2020-07-31T04:25:33.411321+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws create route table for vpc and region

```bash
aws ec2 create-route-table --vpc-id $AWS_VPC_ID --region $AWS_REGION

```

## Expected Output

```
aws ec2 create-route-table --vpc-id vpc-010123123 --region us-east-1
```
