---
id: a2fbbd65-ee84-4009-869b-a3e409a58863
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:19.794705+00:00'
updated_at: '2023-04-10T20:36:41.018201+00:00'
---

# Code Snippet a2fbbd65

**Language**: ps1

```ps1
Get-SQLInstanceDomain -Verbose
# Get Server Info for Found Instances
Get-SQLInstanceDomain | Get-SQLServerInfo -Verbose
# Get Database Names
Get-SQLInstanceDomain | Get-SQLDatabase -NoDefaults
```


