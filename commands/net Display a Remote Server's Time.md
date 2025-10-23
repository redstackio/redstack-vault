---
id: 8cd9c425-1b5d-44bf-be71-1ac1759aa8d8
name: net Display a Remote Server's Time
type: command
executor: bash
data: net time -S $_TARGET_IP
output: 'root@kali:~# net time -S 10.10.10.5

  Wed Jun 24 20:16:26 2020'
created_at: '2020-06-25T00:16:01.496565+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# net Display a Remote Server's Time

```bash
net time -S $_TARGET_IP
```

## Expected Output

```
root@kali:~# net time -S 10.10.10.5
Wed Jun 24 20:16:26 2020
```


