---
id: 73d8e933-46f3-40f3-9193-a8d93a84d480
name: Associate IAM instance profile with EC2 instance
type: command
executor: bash
data: aws ec2 associate-iam-instance-profile --iam-instance-profile Name=admin-role
  --instance-id i-0123456789
output: null
created_at: '2023-04-06T03:56:09.317722+00:00'
updated_at: '2023-04-10T20:19:54.703524+00:00'
---

# Associate IAM instance profile with EC2 instance

```bash
aws ec2 associate-iam-instance-profile --iam-instance-profile Name=admin-role --instance-id i-0123456789
```
