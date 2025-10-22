---
id: d3a65bdc-47dc-4abf-bca5-d6d35143a533
name: Enumerate domain machines of the current/specified domain where specific users
  are logged into
type: command
executor: bash
data: Find-DomainUserLocation -Domain <DomainName> | Select-Object UserName, SessionFromName
output: null
created_at: '2023-04-06T03:56:02.229419+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
---

# Enumerate domain machines of the current/specified domain where specific users are logged into

```bash
Find-DomainUserLocation -Domain <DomainName> | Select-Object UserName, SessionFromName
```
