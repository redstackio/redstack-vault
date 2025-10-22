---
id: 8f78582c-9cfa-4f63-8a7c-a58720efa994
name: Linux Service Information
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:45.441488+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Linux Service Information

**Command** ([[View processes in branch form]]):

```bash
ps auxwff

```

**Command** ([[View processes in branch form]]):

```bash
pstree -A -p

```

**Command** ([[View processes running as root]]):

```bash
ps aux | grep root

```

**Command** ([[Lookup process binary path and permissions]]):

```bash
ps aux | awk '{print $11}'|xargs -r ls -la 2>/dev/null |awk '!x[$0]++'
cat /etc/inetd.conf
cat /etc/xinetd.conf

```

**Command** ([[Show extrated binaries]]):

```bash
cat /etc/xinetd.conf 2>/dev/null | awk '{print $7}' |xargs -r ls -la 2>/dev/null

```

**Command** ([[Permissions and contents of /etc/exports (NFS)]]):

```bash
ls -la /etc/exports 2>/dev/null; cat /etc/exports 2>/dev/null

```
