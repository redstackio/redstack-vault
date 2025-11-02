---
id: 72d514b3-35d8-4732-ab46-b9105b060e12
name: xxd Convert Hex Dump to Binary
type: command
executor: bash
data: xxd -ps -r $_INPUT > $_OUTPUT
output: xxd -ps -r dump  > dump.decoded
created_at: '2019-11-25T19:19:33.877757+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[ps]]'
- '[[xxd]]'
---

# xxd Convert Hex Dump to Binary

```bash
xxd -ps -r $_INPUT > $_OUTPUT
```

## Expected Output

```
xxd -ps -r dump  > dump.decoded
```


