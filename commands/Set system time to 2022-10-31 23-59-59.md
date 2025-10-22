---
id: 56625a29-e6c3-4fa7-b538-620f49cdeef0
name: Set system time to 2022-10-31 23:59:59
type: command
executor: bash
data: 'ORIG_TIME=$(date)

  date -s "2022-10-31 23:59:59"

  touch -a -m "example"

  date -s "${ORIG_TIME}"'
output: null
created_at: '2023-04-06T03:56:17.809041+00:00'
updated_at: '2023-04-10T20:34:10.431707+00:00'
---

# Set system time to 2022-10-31 23:59:59

```bash
ORIG_TIME=$(date)
date -s "2022-10-31 23:59:59"
touch -a -m "example"
date -s "${ORIG_TIME}"
```
