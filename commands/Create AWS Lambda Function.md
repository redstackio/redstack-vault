---
id: f5ab9496-7240-4715-af1e-9ac1d1629671
name: Create AWS Lambda Function
type: command
executor: bash
data: aws lambda create-function --function-name my-function --runtime python3.7 --zip-file
  fileb://my-function.zip --handler my-function.handler --role ARN --region region
output: null
created_at: '2023-04-06T03:56:11.980420+00:00'
updated_at: '2023-04-10T20:20:06.347542+00:00'
---

# Create AWS Lambda Function

```bash
aws lambda create-function --function-name my-function --runtime python3.7 --zip-file fileb://my-function.zip --handler my-function.handler --role ARN --region region
```
