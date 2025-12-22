---
id: cmd-uuid-007
data: sudo ./nebula -config config.yml
tags:
  - trigger
  - exploit
type: command
output: Nebula startup logs
executor: bash
platforms:
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.845Z'
verified: false
validated: true
submitted: true
---
# sudo-nebula-run

## Command

```bash
sudo ./nebula -config config.yml
```

## Description

Runs the Nebula client with sudo using a config file, triggering vulnerable exec calls.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-config` | Path to config.yml | Yes |
| `config.yml` | Configuration file | Yes |

## Examples

### Basic Usage

```bash
sudo ./nebula -config config.yml
```

### Advanced Usage

```bash
sudo ./nebula -config /path/to/config.yml --debug
```

## Expected Output

Nebula initialization logs; triggers ifconfig call leading to shell.

## Related

- [[procedures/Exploit-Nebula-PATH-Hijacking-for-RCE]]
