---
id: 700a5197-ac55-47fd-888f-4f866b5a7acc
name: showmount List NFS Exports
type: command
executor: bash
data: showmount -e $_TARGET_IP
output: 'root@kali:~# showmount -e 10.10.10.10

  Export list for 10.10.10.10:

  / *'
created_at: '2019-09-18T21:37:17.799869+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[showmount]]'
---

# showmount List NFS Exports

```bash
showmount -e $_TARGET_IP
```

## Expected Output

```
root@kali:~# showmount -e 10.10.10.10
Export list for 10.10.10.10:
/ *
```


