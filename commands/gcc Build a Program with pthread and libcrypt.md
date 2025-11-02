---
id: 972635eb-dd8f-4684-8aa7-d16e4d026505
name: gcc Build a Program with pthread and libcrypt
type: command
executor: bash
data: gcc $_INPUT.c -pthread -lcrypt -o $_OUTPUT
output: root@kali:~# gcc dirty.c -pthread -lcrypt -o dirty
created_at: '2019-11-15T21:04:23.842238+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[GCC]]'
---

# gcc Build a Program with pthread and libcrypt

```bash
gcc $_INPUT.c -pthread -lcrypt -o $_OUTPUT
```

## Expected Output

```
root@kali:~# gcc dirty.c -pthread -lcrypt -o dirty
```


