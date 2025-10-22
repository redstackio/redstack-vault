---
id: 2ccd1fa6-61a7-4ca1-9aac-82c2e74cb29a
name: Creating A VPC
type: command
executor: bash
data: 'aws ec2 create-vpc --cidr-block <cidr_block> --regiosn <region>

  '
output: aws ec2 create-vpc --cidr-block 10.0.0.0/16 --region eu-west-1
created_at: '2020-07-31T04:25:22.966125+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Creating A VPC

```bash
aws ec2 create-vpc --cidr-block <cidr_block> --regiosn <region>

```

## Expected Output

```
aws ec2 create-vpc --cidr-block 10.0.0.0/16 --region eu-west-1
```
