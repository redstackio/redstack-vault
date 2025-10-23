---
id: d168c6ee-6aa3-460c-a1ad-9afc025d5776
name: Showmount List Mounted NFS Directories
type: command
executor: bash
data: showmount -d $_TARGET_IP
output: 'root@kali:~# showmount -d 10.10.10.12

  Directories on 10.10.10.12:

  /'
created_at: '2019-09-11T21:53:20.838942+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Showmount List Mounted NFS Directories

```bash
showmount -d $_TARGET_IP
```

## Expected Output

```
root@kali:~# showmount -d 10.10.10.12
Directories on 10.10.10.12:
/
```


