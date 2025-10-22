---
id: 986d6a38-ec3f-4e67-b6f5-268f5566735f
name: Get etcd keys
type: command
executor: bash
data: etcdctl --endpoints=http://<MASTER-IP>:2379 get / --prefix --keys-only
output: null
created_at: '2023-04-06T03:56:01.482594+00:00'
updated_at: '2023-04-10T20:34:02.112361+00:00'
---

# Get etcd keys

```bash
etcdctl --endpoints=http://<MASTER-IP>:2379 get / --prefix --keys-only
```
