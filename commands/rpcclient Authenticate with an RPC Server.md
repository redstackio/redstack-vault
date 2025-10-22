---
id: 33ff043a-6e43-4561-ab56-91233e200a36
name: rpcclient Authenticate with an RPC Server
type: command
executor: bash
data: rpcclient -U "$_USERNAME%$_PASSWORD" $_TARGET_IP
output: rpcclient -U "bob%secretpass" 10.10.10.10
created_at: '2019-09-18T23:26:06.918339+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# rpcclient Authenticate with an RPC Server

```bash
rpcclient -U "$_USERNAME%$_PASSWORD" $_TARGET_IP
```

## Expected Output

```
rpcclient -U "bob%secretpass" 10.10.10.10
```
