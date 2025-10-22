---
id: a2aa9762-1897-40e4-9345-ac4dc7b3602c
name: Docker Login to AWS ECR
type: command
executor: bash
data: aws ecr get-login-password --region region | docker login --username AWS --password-stdin
  ecr_address
output: null
created_at: '2023-04-06T03:56:13.114768+00:00'
updated_at: '2023-04-10T20:20:00.280942+00:00'
---

# Docker Login to AWS ECR

```bash
aws ecr get-login-password --region region | docker login --username AWS --password-stdin ecr_address
```
