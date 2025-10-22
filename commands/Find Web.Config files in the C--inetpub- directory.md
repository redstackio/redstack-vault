---
id: f154d5f9-b2a2-4ae1-b882-23ac7966edb0
name: Find Web.Config files in the C:\inetpub\ directory
type: command
executor: bash
data: Get-Childitem –Path C:\inetpub\ -Include web.config -File -Recurse -ErrorAction
  SilentlyContinue
output: null
created_at: '2023-04-06T03:56:29.120409+00:00'
updated_at: '2023-04-10T20:37:44.587367+00:00'
---

# Find Web.Config files in the C:\inetpub\ directory

```bash
Get-Childitem –Path C:\inetpub\ -Include web.config -File -Recurse -ErrorAction SilentlyContinue
```
