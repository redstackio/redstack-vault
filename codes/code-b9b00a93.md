---
id: b9b00a93-4163-4972-88b8-fc606c199088
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:09.319132+00:00'
updated_at: '2023-04-10T20:19:54.707071+00:00'
---

# Code Snippet b9b00a93

**Language**: Powershell

```powershell
$ aws lambda create-function –function-name my_function –runtime python3.6 –role arn_of_lambda_role –handler lambda_function.lambda_handler –code file://my/python/code.py
$ aws lambda invoke –function-name my_function output.txt
```


