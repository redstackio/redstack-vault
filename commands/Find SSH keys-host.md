---
id: d75493d1-6807-41c7-8129-118b59444ccb
name: Find SSH keys/host
type: command
executor: bash
data: 'find / -name "id_dsa*" -o -name "id_rsa*" -o -name "known_hosts" -o -name "authorized_hosts"
  -o -name "authorized_keys" 2>/dev/null |xargs -r ls -la

  '
output: null
created_at: '2020-07-14T18:14:41.287336+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Find SSH keys/host

```bash
find / -name "id_dsa*" -o -name "id_rsa*" -o -name "known_hosts" -o -name "authorized_hosts" -o -name "authorized_keys" 2>/dev/null |xargs -r ls -la

```
