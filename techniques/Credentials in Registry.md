---
id: 910bff51-9ae6-4880-88f3-cb7fc59a6b2a
name: Credentials in Registry
type: technique
mitre_id: T1214
mitre_url: null
created_at: '2019-08-28T21:17:46.338129+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[Github API Key Leakage]]'
- '[[Github API Key Leakage]]'
- '[[Github API Key Leakage]]'
- '[[Kerberos Constrained Delegation Exploitation]]'
- '[[Server-Side Request Forgery (SSRF) Exploitation via PDF Files]]'
- '[[Windows Credentials Decryption using Powershell Secure String]]'
- '[[Windows - EoP Looting for Passwords via Key Manager]]'
- '[[Windows Privilege Escalation - Looting LAPS Settings]]'
- '[[Windows Vault Credential Theft with Mimikatz]]'
---

# Credentials in Registry

**MITRE ID**: T1214

## Description

The Windows Registry stores configuration information that can be used by the system or other programs. Adversaries may query the Registry looking for credentials and passwords that have been stored for use by other programs or services. Sometimes these credentials are used for automatic logons.Example commands to find Registry keys related to password information: [1]Local Machine Hive: reg query HKLM /f password /t REG_SZ /sCurrent User Hive: reg query HKCU /f password /t REG_SZ /s

# Detection

Monitor processes for applications that can be used to query the Registry, such as Reg, and collect command parameters that may indicate credentials are being searched. Correlate activity with related suspicious behavior that may indicate an active intrusion to reduce false positives.

# Mitigation

Do not store credentials within the Registry. Proactively search for credentials within Registry keys and attempt to remediate the risk. If necessary software must store credentials, then ensure those accounts have limited permissions so they cannot be abused if obtained by an adversary.

# Footnotes

[1] netbiosX. (2017, April 19). Stored Credentials. Retrieved April 6, 2018.

[2] Llimos, N., Pascual, C.. (2019, February 12). Trickbot Adds Remote Application Credential-Grabbing Capabilities to Its Repertoire. Retrieved March 12, 2019.

## Defense

Do not store credentials within the Registry. Proactively search for credentials within Registry keys and attempt to remediate the risk. If necessary software must store credentials, then ensure those accounts have limited permissions so they cannot be ab

## Tactics

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures (9)

- [[Github API Key Leakage]]
- [[Github API Key Leakage]]
- [[Github API Key Leakage]]
- [[Kerberos Constrained Delegation Exploitation]]
- [[Server-Side Request Forgery (SSRF) Exploitation via PDF Files]]
- [[Windows Credentials Decryption using Powershell Secure String]]
- [[Windows - EoP Looting for Passwords via Key Manager]]
- [[Windows Privilege Escalation - Looting LAPS Settings]]
- [[Windows Vault Credential Theft with Mimikatz]]
