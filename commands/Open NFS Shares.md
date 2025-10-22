---
id: af7bddba-8f34-469f-86e2-456bb03b3e86
name: Open NFS Shares
type: command
executor: bash
data: 'nmap -p 111,2049 --script nfs-ls,nfs-showmount

  '
output: null
created_at: '2020-07-14T18:21:14.334778+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Open NFS Shares

```bash
nmap -p 111,2049 --script nfs-ls,nfs-showmount

```
