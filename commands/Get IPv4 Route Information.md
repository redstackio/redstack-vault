---
id: 0b334e11-c429-4b71-a698-521e54397a7f
name: Get IPv4 Route Information
type: command
executor: bash
data: Get-NetRoute -AddressFamily IPv4 | ft DestinationPrefix,NextHop,RouteMetric,ifIndex
output: null
created_at: '2023-04-06T03:56:28.696182+00:00'
updated_at: '2023-04-10T20:37:53.209844+00:00'
---

# Get IPv4 Route Information

```bash
Get-NetRoute -AddressFamily IPv4 | ft DestinationPrefix,NextHop,RouteMetric,ifIndex
```


