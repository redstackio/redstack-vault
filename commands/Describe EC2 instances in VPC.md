---
id: 83a666bf-c0d4-4f52-a3b1-09c74c53afad
name: Describe EC2 instances in VPC
type: command
executor: bash
data: aws ec2 describe-instances --filters "Name=vpc-id,Values=ID"
output: null
created_at: '2023-04-06T03:56:14.507020+00:00'
updated_at: '2023-04-10T20:20:17.691315+00:00'
---

# Describe EC2 instances in VPC

```bash
aws ec2 describe-instances --filters "Name=vpc-id,Values=ID"
```


