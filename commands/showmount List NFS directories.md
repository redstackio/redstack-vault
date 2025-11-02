---
id: dd0b9a67-2c47-4055-9f11-fb0432949ddd
name: showmount List NFS directories
type: command
executor: ''
data: showmount -d $_TARGET_IP
output: 'root@kali:~# showmount -d 10.10.10.10

  Directories on 10.10.10.10:

  /'
created_at: '2019-09-18T21:37:17.813549+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[showmount]]'
---

# showmount List NFS directories

```bash
showmount -d $_TARGET_IP
```

## Expected Output

```
root@kali:~# showmount -d 10.10.10.10
Directories on 10.10.10.10:
/
```


