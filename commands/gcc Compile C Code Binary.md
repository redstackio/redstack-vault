---
id: 725d499e-30f5-4584-92fa-65ebb36f4ca3
name: gcc Compile C Code Binary
type: command
executor: bash
data: gcc -o suid suid.c
output: 'root@hackers:~# gcc -o suid suid.c

  root@hackers:~# ./suid

  # '
created_at: '2019-09-17T20:10:55.530193+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[GCC]]'
---

# gcc Compile C Code Binary

```bash
gcc -o suid suid.c
```

## Expected Output

```
root@hackers:~# gcc -o suid suid.c
root@hackers:~# ./suid
# 
```


