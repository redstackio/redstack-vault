---
id: fd8d17b7-8628-492c-afba-ff51f2f6e1c6
name: Get AWS Lambda Function Code Location
type: command
executor: bash
data: $ aws lambda get-function --function-name "LAMBDA-NAME-HERE-FROM-PREVIOUS-QUERY"
  --query 'Code.Location' --profile uploadcreds
output: null
created_at: '2023-04-06T03:56:09.663059+00:00'
updated_at: '2023-04-10T20:19:52.665195+00:00'
---

# Get AWS Lambda Function Code Location

```bash
$ aws lambda get-function --function-name "LAMBDA-NAME-HERE-FROM-PREVIOUS-QUERY" --query 'Code.Location' --profile uploadcreds
```


