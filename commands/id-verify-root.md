---
data: id
tags:
  - verify
  - root
type: command
output: 'uid=1000(user) gid=1000(user) euid=0(root) groups=1000(user),998(nordvpn)'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.150Z'
id: 99790215-2aac-4d1d-bdbb-cc5c1d7c85ba
verified: false
validated: true
submitted: true
---
# id-verify-root

## Command

```bash
id
```

## Description

Displays current user and group IDs, confirming effective UID is 0 (root) after SUID execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| id | Show user identity | Yes |

## Examples

### Basic Usage

```bash
id
```

### Advanced Usage

```bash
id -u  # Just UID
```

## Expected Output

uid=1000(user) gid=1000(user) euid=0(root) groups=1000(user),998(nordvpn), indicating escalation.

## Related

- [[commands/execute-suid-bash]]
- [[procedures/Execute-SUID-Bash-for-Root-Access]]
