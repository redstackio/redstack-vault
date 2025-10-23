---
id: 15e60f1b-5e64-451e-9caf-e617f7570b78
name: Lookup process binary path and permissions
type: command
executor: bash
data: 'ps aux | awk ''{print $11}''|xargs -r ls -la 2>/dev/null |awk ''!x[$0]++''

  cat /etc/inetd.conf

  cat /etc/xinetd.conf

  '
output: null
created_at: '2020-07-14T18:14:44.763901+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Lookup process binary path and permissions

```bash
ps aux | awk '{print $11}'|xargs -r ls -la 2>/dev/null |awk '!x[$0]++'
cat /etc/inetd.conf
cat /etc/xinetd.conf

```


