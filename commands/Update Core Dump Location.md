---
id: 23b0da6f-abb4-4c29-8639-61d043083cde
name: Update Core Dump Location
type: command
executor: bash
data: echo "|/var/lib/docker/overlay2/c51a87501842b287018d22e9d09d7d8dc4ede83a867f36ca199434d5ea5ac8f5/diff/poc"
  > /proc/sys/kernel/core_pattern
output: null
created_at: '2023-04-06T03:56:17.157289+00:00'
updated_at: '2023-04-10T20:33:47.322105+00:00'
---

# Update Core Dump Location

```bash
echo "|/var/lib/docker/overlay2/c51a87501842b287018d22e9d09d7d8dc4ede83a867f36ca199434d5ea5ac8f5/diff/poc" > /proc/sys/kernel/core_pattern
```


