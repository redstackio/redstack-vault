---
id: eaa0a534-7f31-4ae5-aa2e-ebef78efb641
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:01.333948+00:00'
updated_at: '2023-04-10T20:34:06.540658+00:00'
---

# Code Snippet eaa0a534

**Language**: Powershell

```powershell
curl -k -v -XGET -H "Authorization: Bearer <JWT TOKEN (of the impersonator)>" -H "Impersonate-Group: system:masters" -H "Impersonate-User: null" -H "Accept: application/json" https://<master_ip>:<port>/api/v1/namespaces/kube-system/secrets/
```


