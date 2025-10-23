---
id: acc5cb29-1403-4b79-9f83-c9bdb99e0923
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:01.357527+00:00'
updated_at: '2023-04-10T20:33:59.622876+00:00'
---

# Code Snippet acc5cb29

**Language**: Powershell

```powershell
$ cat /run/secrets/kubernetes.io/serviceaccount/token
$ curl -k -v -H "Authorization: Bearer <jwt_token>" https://<master_ip>:<port>/api/v1/namespaces/default/secrets/
```


