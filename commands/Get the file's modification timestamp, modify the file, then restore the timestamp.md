---
id: f0cb2025-7799-4b4b-945c-ec0a14e48e36
name: Get the file's modification timestamp, modify the file, then restore the timestamp
type: command
executor: bash
data: 'MODIFIED_TS=$(stat --format="%Y" "example")

  echo "backdoor" >> "example"

  touch -a -m -d @$MODIFIED_TS "example"'
output: null
created_at: '2023-04-06T03:56:17.808773+00:00'
updated_at: '2023-04-10T20:34:10.431707+00:00'
---

# Get the file's modification timestamp, modify the file, then restore the timestamp

```bash
MODIFIED_TS=$(stat --format="%Y" "example")
echo "backdoor" >> "example"
touch -a -m -d @$MODIFIED_TS "example"
```
