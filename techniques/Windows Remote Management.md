---
id: c250b3a1-e523-4796-832a-03720fdd7f20
name: Windows Remote Management
type: technique
mitre_id: T1028
mitre_url: null
created_at: '2019-08-28T21:17:42.191078+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
procedures:
- '[[Connect to WinRM from a Linux System (Pass-the-Hash)]]'
- '[[Execute a Command on a Remote System with WinRM]]'
- '[[Image-Based .htaccess Upload]]'
- '[[Remote access to Windows Machine (credentials)]]'
- '[[Spawn an Interactive Shell with WinRM (Linux)]]'
- '[[Spawn an Interactive Shell with WinRM (Windows)]]'
---

# Windows Remote Management

**MITRE ID**: T1028

## Description

Windows Remote Management (WinRM) is the name of both a Windows service and a protocol that allows a user to interact with a remote system (e.g., run an executable, modify the Registry, modify services). [1] It may be called with the winrm command or by any number of programs such as PowerShell. [2]

# Detection

Monitor use of WinRM within an environment by tracking service execution. If it is not normally used or is disabled, then this may be an indicator of suspicious behavior. Monitor processes created and actions taken by the WinRM process or a WinRM invoked script to correlate it with other related events.

# Mitigation

Disable the WinRM service. If the service is necessary, lock down critical enclaves with separate WinRM infrastructure, accounts, and permissions. Follow WinRM best practices on configuration of authentication methods and use of host firewalls to restrict WinRM access to allow communication only to/from specific devices. [5]

# Footnotes

[1] Microsoft. (n.d.). Windows Remote Management. Retrieved November 12, 2014.

[2] Jacobsen, K. (2014, May 16). Lateral Movement with PowerShell[slides]. Retrieved November 12, 2014.

[3] Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.

[4] Counter Threat Unit Research Team. (2017, June 27). BRONZE UNION Cyberespionage Persists Despite Disclosures. Retrieved July 13, 2017.

[5] National Security Agency/Central Security Service Information Assurance Directorate. (2015, August 7). Spotting the Adversary with Windows Event Log Monitoring. Retrieved September 6, 2018.

## Defense

Disable the WinRM service. If the service is necessary, lock down critical enclaves with separate WinRM infrastructure, accounts, and permissions. Follow WinRM best practices on configuration of authentication methods and use of host firewalls to restrict

## Tactics

- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

## Related Procedures (6)

- [[Connect to WinRM from a Linux System (Pass-the-Hash)]]
- [[Execute a Command on a Remote System with WinRM]]
- [[Image-Based .htaccess Upload]]
- [[Remote access to Windows Machine (credentials)]]
- [[Spawn an Interactive Shell with WinRM (Linux)]]
- [[Spawn an Interactive Shell with WinRM (Windows)]]
