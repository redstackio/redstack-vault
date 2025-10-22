---
id: 95ccb578-4210-4807-a594-93d6386f3339
name: Password Filter DLL
type: technique
mitre_id: T1174
mitre_url: null
created_at: '2019-08-28T21:17:40.755027+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[Active Directory ACLs/ACEs Password Reset]]'
- '[[Password Extraction from SYSVOL and Group Policy Preferences]]'
- '[[Windows Password Looting via File Contents Search]]'
- '[[Windows Privilege Escalation via IIS Web Config Looting]]'
- '[[Windows - SAM and SYSTEM Hash Extraction]]'
---

# Password Filter DLL

**MITRE ID**: T1174

## Description

Windows password filters are password policy enforcement mechanisms for both domain and local accounts. Filters are implemented as dynamic link libraries (DLLs) containing a method to validate potential passwords against password policies. Filter DLLs can be positioned on local computers for local accounts and/or domain controllers for domain accounts.Before registering new passwords in the Security Accounts Manager (SAM), the Local Security Authority (LSA) requests validation from each registered filter. Any potential changes cannot take effect until every registered filter acknowledges validation.Adversaries can register malicious password filters to harvest credentials from local computers and/or entire domains. To perform proper validation, filters must receive plain-text credentials from the LSA. A malicious password filter would receive these plain-text credentials every time a password request is made. [1]

# Detection

Monitor for change notifications to and from unfamiliar password filters.

Newly installed password filters will not take effect until after a system reboot.

Password filters will show up as an autorun and loaded DLL in lsass.exe. [4]

# Mitigation

Ensure only valid password filters are registered. Filter DLLs must be present in Windows installation directory (C:\Windows\System32\ by default) of a domain controller and/or local computer with a corresponding entry in HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\Notification Packages. [3]

# Footnotes

[1] Fuller, R. (2013, September 11). Stealing passwords every time they change. Retrieved November 21, 2017.

[2] Kaspersky Lab's Global Research & Analysis Team. (2016, August 9). The ProjectSauron APT. Retrieved August 17, 2016.

[3] Microsoft. (n.d.). Installing and Registering a Password Filter DLL. Retrieved November 21, 2017.

[4] Bialek, J. (2013, September 15). Intercepting Password Changes With Function Hooking. Retrieved November 21, 2017.

## Defense

Ensure only valid password filters are registered. Filter DLLs must be present in Windows installation directory (<code>C:\Windows\System32\</code> by default) of a domain controller and/or local computer with a corresponding entry in <code>HKEY_LOCAL_MAC

## Tactics

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures (5)

- [[Active Directory ACLs/ACEs Password Reset]]
- [[Password Extraction from SYSVOL and Group Policy Preferences]]
- [[Windows Password Looting via File Contents Search]]
- [[Windows Privilege Escalation via IIS Web Config Looting]]
- [[Windows - SAM and SYSTEM Hash Extraction]]
