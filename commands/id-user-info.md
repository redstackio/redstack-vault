---
id: uuid-id-command
data: id
tags:
  - recon
  - user-info
type: command
output: uid=999(solr) gid=999(solr) groups=999(solr)
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.324Z'
verified: false
validated: true
submitted: true
---
# id-user-info

## Command

```bash
id
```

## Description

Displays user and group IDs for the current user, useful in RCE scenarios to identify privileges and potential escalation paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; shows current user info | No |

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

uid=999(solr) gid=999(solr) groups=999(solr)

## Related

- [[commands/whoami]]
- [[procedures/Exploit-Solr-Velocity-RCE-ID-Command]]
