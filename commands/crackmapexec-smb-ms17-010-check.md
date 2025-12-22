---
type: command
executor: bash
data: crackmapexec smb <target_ip> -u '' -p '' -d . -M ms17-010
tags:
  - exploitation
  - smb
  - vulnerability-check
platforms:
  - Linux
verified: true
validated: true
---

# crackmapexec-smb-ms17-010-check

## Command

```bash
crackmapexec smb <target_ip> -u '' -p '' -d . -M ms17-010
```

## Description

This CrackMapExec command checks a specific host for the MS17-010 EternalBlue vulnerability using the ms17-010 module, performing an unauthenticated probe to assess RCE potential.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <target_ip> | IP address of the target | Yes |
| -u '' | Empty username for unauthenticated check | Yes |
| -p '' | Empty password | Yes |
| -d . | Local domain | Yes |
| -M ms17-010 | Use the EternalBlue detection module | Yes |

## Examples

### Basic Usage

```bash
crackmapexec smb 10.10.10.10 -u '' -p '' -d . -M ms17-010
```

### Advanced Usage

```bash
crackmapexec smb 10.10.10.10 -u guest -p password -d WORKGROUP -M ms17-010 --verbose
```

## Expected Output

```
SMB         10.10.10.10    445    TARGET          [*] Windows 7 Professional 7601 Service Pack 1 (language:English)
SMB         10.10.10.10    445    TARGET          [+] TARGET\$ (Pwn3d!):
SMB         10.10.10.10    445    TARGET          [MS17-010] Remote Code Execution Vulnerability (EternalBlue)
```

## Related

- [[procedures/EternalBlue-SMB-Exploitation]]
- [[tools/CrackMapExec]]
