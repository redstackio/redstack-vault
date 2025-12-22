---
id: cmd-uuid-2
data: id
tags:
  - recon
  - exfiltration
type: command
output: uid=33(www-data) gid=33(www-data) groups=33(www-data)
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.127Z'
verified: false
validated: true
submitted: true
---
# id-exfiltrate

## Command

```bash
id
```

## Description

Displays the current user and group identities, used in this context to exfiltrate server user information (e.g., confirming www-data privileges) via injection in a blind RCE scenario.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters | No |

## Examples

### Basic Usage

```bash
id
```

### Advanced Usage

```bash
id -u  # User ID only
```

## Expected Output

uid=33(www-data) gid=33(www-data) groups=33(www-data) – output captured and exfiltrated via wget in the payload.

## Related

- [[commands/wget-exfiltrate-id]]
