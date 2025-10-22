---
id: ff319344-fc19-4b9d-938d-dab3ef210efc
name: Check Group Membership of a User
type: command
executor: bash
data: groups $USER
output: 'root@kali:~# groups alice

  alice : alice docker'
created_at: '2019-10-09T19:15:07.838682+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Check Group Membership of a User

```bash
groups $USER
```

## Expected Output

```
root@kali:~# groups alice
alice : alice docker
```
