---
id: 197d4d94-5c10-4311-933f-d44d4fcf49cf
name: Associate IAM Instance Profile
type: command
executor: bash
data: aws ec2 associate-iam-instance-profile --instance-id ID --iam-instance-profile
  Name=ProfileName
output: null
created_at: '2023-04-06T03:56:13.529718+00:00'
updated_at: '2023-04-10T20:20:54.124879+00:00'
---

# Associate IAM Instance Profile

```bash
aws ec2 associate-iam-instance-profile --instance-id ID --iam-instance-profile Name=ProfileName
```
