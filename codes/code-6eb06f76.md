---
id: 6eb06f76-724c-438b-a5a0-ae0cfcfee353
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:09.662834+00:00'
updated_at: '2023-04-10T20:19:52.667548+00:00'
---

# Code Snippet 6eb06f76

**Language**: Powershell

```powershell
# https://blog.appsecco.com/getting-shell-and-data-access-in-aws-by-chaining-vulnerabilities-7630fa57c7ed
$ aws lambda list-functions --profile uploadcreds
$ aws lambda get-function --function-name "LAMBDA-NAME-HERE-FROM-PREVIOUS-QUERY" --query 'Code.Location' --profile uploadcreds
$ wget -O lambda-function.zip url-from-previous-query --profile uploadcreds
```


