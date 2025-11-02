---
id: d41f0910-0f17-44da-b7cd-e36498bff1e8
name: tmux Attach to a Socket
type: command
executor: bash
data: tmux -S $_PATH/TO/SOCKET/FILE
output: 'dj@Cupid:~$ tmux -S /.devs/dev_sess

  root@Cupid:/#'
created_at: '2019-11-25T21:35:19.511335+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[tmux]]'
---

# tmux Attach to a Socket

```bash
tmux -S $_PATH/TO/SOCKET/FILE
```

## Expected Output

```
dj@Cupid:~$ tmux -S /.devs/dev_sess
root@Cupid:/#
```


