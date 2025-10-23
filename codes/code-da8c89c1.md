---
id: da8c89c1-4387-47ca-9cd9-30144e7f38dd
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:01.482423+00:00'
updated_at: '2023-04-10T20:34:02.115097+00:00'
---

# Code Snippet da8c89c1

**Language**: Powershell

```powershell
curl -k https://<IP address>:2379
curl -k https://<IP address>:2379/version
etcdctl --endpoints=http://<MASTER-IP>:2379 get / --prefix --keys-only
```


