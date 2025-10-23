---
id: 9c7a7247-2788-4191-a085-c040b36bebe2
name: Show extrated binaries
type: command
executor: bash
data: 'cat /etc/xinetd.conf 2>/dev/null | awk ''{print $7}'' |xargs -r ls -la 2>/dev/null

  '
output: null
created_at: '2020-07-14T18:14:44.764301+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Show extrated binaries

```bash
cat /etc/xinetd.conf 2>/dev/null | awk '{print $7}' |xargs -r ls -la 2>/dev/null

```


