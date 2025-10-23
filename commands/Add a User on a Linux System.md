---
id: 55a2a922-84a7-4ea4-a16b-a5b7687fa2c6
name: Add a User on a Linux System
type: command
executor: bash
data: adduser $_NAME
output: 'root@a7ffb5e7e757:/tmp# adduser alice

  Adding user `alice'' ...

  Adding new group `alice'' (1001) ...

  Adding new user `alice'' (1001) with group `alice'' ...

  Creating home directory `/home/alice'' ...'
created_at: '2020-03-10T09:00:42.694827+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Add a User on a Linux System

```bash
adduser $_NAME
```

## Expected Output

```
root@a7ffb5e7e757:/tmp# adduser alice
Adding user `alice' ...
Adding new group `alice' (1001) ...
Adding new user `alice' (1001) with group `alice' ...
Creating home directory `/home/alice' ...
```


