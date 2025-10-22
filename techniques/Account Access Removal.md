---
id: 01a85693-0756-4fd7-a68d-6fe8a4634058
name: Account Access Removal
type: technique
mitre_id: T1531
mitre_url: null
created_at: '2023-04-06T00:31:26.753678+00:00'
updated_at: '2023-04-06T03:56:38.418990+00:00'
tactics:
- '[[Impact|TA0040 - Impact]]'
procedures:
- '[[SSRF for AWS Metadata and User Data Commands]]'
- '[[SSRF URL for Google Cloud Instances - Add SSH Key]]'
---

# Account Access Removal

**MITRE ID**: T1531

## Description

Adversaries may interrupt availability of system and network resources by inhibiting access to accounts utilized by legitimate users. Accounts may be deleted, locked, or manipulated (ex: changed credentials) to remove access to accounts. Adversaries may also subsequently log off and/or perform a [System Shutdown/Reboot](https://attack.mitre.org/techniques/T1529) to set malicious changes into place.(Citation: CarbonBlack LockerGoga 2019)(Citation: Unit42 LockerGoga 2019)

In Windows, [Net](https://attack.mitre.org/software/S0039) utility, <code>Set-LocalUser</code> and <code>Set-ADAccountPassword</code> [PowerShell](https://attack.mitre.org/techniques/T1059/001) cmdlets may be used by adversaries to modify user accounts. In Linux, the <code>passwd</code> utility may be used to change passwords. Accounts could also be disabled by Group Policy. 

Adversaries who use ransomware may first perform this and other Impact behaviors, such as [Data Destruction](https://attack.mitre.org/techniques/T1485) and [Defacement](https://attack.mitre.org/techniques/T1491), before completing the [Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486) objective. 

## Tactics

- [[Impact|TA0040 - Impact]]

## Related Procedures (2)

- [[SSRF for AWS Metadata and User Data Commands]]
- [[SSRF URL for Google Cloud Instances - Add SSH Key]]
