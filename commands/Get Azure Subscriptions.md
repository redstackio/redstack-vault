---
id: f2d37499-c56a-42f6-8d02-3e8438c2b225
name: Get Azure Subscriptions
type: command
executor: bash
data: "$Token = 'eyJ0eX..'\n$URI = 'https://management.azure.com/subscriptions?api-version=2020-01-01'\n\
  $RequestParams = @{\n Method = 'GET'\n Uri = $URI\n Headers = @{\n 'Authorization'\
  \ = \"Bearer $Token\"\n }\n}\n"
output: null
created_at: '2023-04-06T03:56:15.188288+00:00'
updated_at: '2023-05-24T08:00:06.101933+00:00'
---

# Get Azure Subscriptions

```bash
$Token = 'eyJ0eX..'
$URI = 'https://management.azure.com/subscriptions?api-version=2020-01-01'
$RequestParams = @{
 Method = 'GET'
 Uri = $URI
 Headers = @{
 'Authorization' = "Bearer $Token"
 }
}

```


