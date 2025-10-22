---
id: 3b6483f0-ee83-4579-94c9-d015de3540f1
name: Create Lambda Function
type: command
executor: bash
data: $ aws lambda create-function –function-name my_function –runtime python3.6 –role
  arn_of_lambda_role –handler lambda_function.lambda_handler –code file://my/python/code.py
output: null
created_at: '2023-04-06T03:56:09.319203+00:00'
updated_at: '2023-04-10T20:19:54.703524+00:00'
---

# Create Lambda Function

```bash
$ aws lambda create-function –function-name my_function –runtime python3.6 –role arn_of_lambda_role –handler lambda_function.lambda_handler –code file://my/python/code.py
```
