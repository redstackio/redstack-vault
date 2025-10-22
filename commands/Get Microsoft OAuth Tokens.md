---
id: 0bdd5904-5acc-41ce-a172-f8b59e3db329
name: Get Microsoft OAuth Tokens
type: command
executor: bash
data: "$body=@{\n    \"client_id\" =  \"1950a258-227b-4e31-a9cf-717495945fc2\"\n \
  \   \"grant_type\" = \"urn:ietf:params:oauth:grant-type:device_code\"\n    \"code\"\
  \ =       $authResponse.device_code\n}\n$Tokens = Invoke-RestMethod `\n    -UseBasicParsing\
  \ `\n    -Method Post `\n    -Uri \"https://login.microsoftonline.com/Common/oauth2/token?api-version=1.0\"\
  \ `\n    -Headers $Headers `\n    -Body $body\n$Tokens"
output: null
created_at: '2023-05-23T16:19:52.223132+00:00'
updated_at: '2023-05-23T16:19:52.247389+00:00'
---

# Get Microsoft OAuth Tokens

```bash
$body=@{
    "client_id" =  "1950a258-227b-4e31-a9cf-717495945fc2"
    "grant_type" = "urn:ietf:params:oauth:grant-type:device_code"
    "code" =       $authResponse.device_code
}
$Tokens = Invoke-RestMethod `
    -UseBasicParsing `
    -Method Post `
    -Uri "https://login.microsoftonline.com/Common/oauth2/token?api-version=1.0" `
    -Headers $Headers `
    -Body $body
$Tokens
```
