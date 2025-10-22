---
id: 63b28b60-15ef-45e6-ae64-c0da74659822
name: Describe EC2 instances in a specific subnet
type: command
executor: bash
data: aws ec2 describe-instances --filters "Name=subnet-id,Values=ID"
output: null
created_at: '2023-04-06T03:56:14.531701+00:00'
updated_at: '2023-04-10T20:20:58.396615+00:00'
---

# Describe EC2 instances in a specific subnet

```bash
aws ec2 describe-instances --filters "Name=subnet-id,Values=ID"
```
