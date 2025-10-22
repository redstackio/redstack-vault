---
id: 2d87e5fa-00b5-45d1-a3b6-3f57a7c7594f
name: Retrieve instance metadata
type: command
executor: bash
data: curl -H Metadata:true http://169.254.169.254/metadata/instance?api-version=2021-02-01
output: null
created_at: '2023-04-06T03:56:38.548180+00:00'
updated_at: '2023-04-10T20:23:56.681624+00:00'
---

# Retrieve instance metadata

```bash
curl -H Metadata:true http://169.254.169.254/metadata/instance?api-version=2021-02-01
```
