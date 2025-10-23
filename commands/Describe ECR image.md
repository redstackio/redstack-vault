---
id: 8c135a0e-4c5c-4b05-ab59-236734c86f2c
name: Describe ECR Image
type: command
executor: bash
data: aws ecr describe-images --repository-name name --image-ids imageTag=Name
output: null
created_at: '2023-04-06T03:56:13.091308+00:00'
updated_at: '2023-04-10T20:20:47.456456+00:00'
---

# Describe ECR Image

```bash
aws ecr describe-images --repository-name name --image-ids imageTag=Name
```


