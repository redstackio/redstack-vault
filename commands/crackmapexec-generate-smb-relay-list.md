---
type: command
executor: bash
data: crackmapexec smb $_HOSTS --gen-relay-list $_OUTPUT_FILE
output: null
platforms:
  - Linux
tags:
  - smb
  - relay
  - enumeration
verified: true
validated: true
---

# crackmapexec-generate-smb-relay-list

## Command

```bash
crackmapexec smb $_HOSTS --gen-relay-list $_OUTPUT_FILE
```

## Description

This command uses CrackMapExec to scan SMB hosts and generate a list of targets vulnerable to NTLM relaying (those without SMB signing enforced). It outputs a file usable by relay tools like ntlmrelayx.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_HOSTS | Target hosts or IP range (e.g., 192.168.1.0/24) | Yes |
| --gen-relay-list | Flag to generate relay target list | Yes |
| $_OUTPUT_FILE | Output file for the relay list (e.g., relay.txt) | Yes |
| smb | Protocol to scan (SMB) | Built-in |

## Examples

### Basic Usage

```bash
crackmapexec smb 192.168.1.0/24 --gen-relay-list relay.txt
```

### Advanced Usage

```bash
crackmapexec smb targets.txt --gen-relay-list vulnerable_relays.txt -u '' -p ''
```

## Expected Output

The command will scan hosts and print progress like:

SMB         192.168.1.10:445 DC01          [+] Windows 10.0 Build 19041 (name:DC01) (Pwn3d!)

Upon completion, relay.txt contains lines like:

192.168.1.10

No signing enforced on listed hosts.

## Related

- [[procedures/SMB-NTLM-Relay-Attack-via-IPv6-with-Disabled-Signing]]
- [[tools/CrackMapExec]]
