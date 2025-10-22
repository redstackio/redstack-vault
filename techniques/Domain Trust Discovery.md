---
id: e8aed4d7-494b-46c5-b7e4-c1ca2196cba2
name: Domain Trust Discovery
type: technique
mitre_id: T1482
mitre_url: null
created_at: '2019-08-28T21:17:26.940966+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
procedures:
- '[[Abusing Active Directory ACLs/ACEs to Retrieve LAPS Passwords]]'
- '[[Active Directory Account Enumeration using CrackMapExec]]'
- '[[Active Directory ACLs/ACEs Password Reset]]'
- '[[Active Directory Assessment and Privilege Escalation]]'
- '[[Active Directory Integrated DNS Enumeration]]'
- '[[Active Directory Recon - Using AD Module]]'
- '[[Active Directory Recon using BloodHound and Certipy]]'
- '[[Active Directory Recon with PowerView]]'
- '[[Active Directory User Enumeration]]'
- '[[Add Domain Admin to RODC Password Replication Group Procedure]]'
- '[[AdminCount Abuse]]'
- '[[Analyze BloodHound Data for Relationships]]'
- '[[Azure Reconnaissance]]'
- '[[Azure Subdomain Enumeration]]'
- '[[Domain Admins Group Access]]'
- '[[Domain Takeover via Certifried CVE-2022-26923]]'
- '[[Establishing and Enumerating PAM Trust between lab.local and bastion.local]]'
- '[[Forest to Forest Trust Ticket Hash Dump]]'
- '[[Forest Trust Ticket Dumping]]'
- '[[Golden Certificate Domain Persistence]]'
- '[[Kerberos Constrained Delegation - Identify Trusted Computers and Delegation Permissions]]'
- '[[Linked Database Crawling for MSSQL Server Enumeration]]'
- '[[Map an Active Directory Environment (SharpHound)]]'
- '[[Query LDAP and Enumerate the Base DN (Nmap)]]'
- '[[Query LDAP for Root DSE Object Information]]'
- '[[samAccountName Spoofing Attack]]'
- '[[Subdomain Enumeration using AltDNS]]'
- '[[Subdomain Enumeration with Findomain]]'
---

# Domain Trust Discovery

**MITRE ID**: T1482

## Description

Adversaries may attempt to gather information on domain trust relationships that may be used to identify Lateral Movement opportunities in Windows multi-domain/forest environments. Domain trusts provide a mechanism for a domain to allow access to resources based on the authentication procedures of another domain.[1] Domain trusts allow the users of the trusted domain to access resources in the trusting domain. The information discovered may help the adversary conduct SID-History Injection, Pass the Ticket, and Kerberoasting.[2][3] Domain trusts can be enumerated using the DSEnumerateDomainTrusts() Win32 API call, .NET methods, and LDAP.[3] The Windows utility Nltest is known to be used by adversaries to enumerate domain trusts.[4]

# Detection

System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation but as part of a chain of behavior that could lead to other activities based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system and network information, such as nltest /domain_trusts. Remote access tools with built-in features may interact directly with the Windows API to gather information. Look for the DSEnumerateDomainTrusts() Win32 API call to spot activity associated with Domain Trust Discovery.[3] Information may also be acquired through Windows system management tools such as PowerShell. The .NET method GetAllTrustRelationships() can be an indicator of Domain Trust Discovery.[11]

# Mitigation

Map the trusts within existing domains/forests and keep trust relationships to a minimum. Employ network segmentation for sensitive domains.[3]

# Footnotes

[1] Microsoft. (2009, October 7). Trust Technologies. Retrieved February 14, 2019.

[2] Metcalf, S. (2015, July 15). It’s All About Trust – Forging Kerberos Trust Tickets to Spoof Access across Active Directory Trusts. Retrieved February 14, 2019.

[3] Schroeder, W. (2017, October 30). A Guide to Attacking Domain Trusts. Retrieved February 14, 2019.

[4] Florio, E.. (2017, May 4). Windows Defender ATP thwarts Operation WilySupply software supply chain cyberattack. Retrieved February 14, 2019.

[5] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[6] ss64. (n.d.). NLTEST.exe - Network Location Test. Retrieved February 14, 2019.

[7] Bacurio Jr., F. and Salvio, J. (2018, April 9). Trickbot’s New Reconnaissance Plugin. Retrieved February 14, 2019.

[8] Nettitude. (2016, June 8). PoshC2: Powershell C2 Server and Implants. Retrieved April 23, 2019.

[9] PowerShellMafia. (2012, May 26). PowerSploit - A PowerShell Post-Exploitation Framework. Retrieved February 6, 2018.

[10] PowerSploit. (n.d.). PowerSploit. Retrieved February 6, 2018.

[11] Microsoft. (n.d.). Domain.GetAllTrustRelationships Method. Retrieved February 14, 2019.

## Defense

Map the trusts within existing domains/forests and keep trust relationships to a minimum. Employ network segmentation for sensitive domains.(Citation: Harmj0y Domain Trusts)

## Tactics

- [[Discovery|TA0007 - Discovery]]

## Related Procedures (28)

- [[Abusing Active Directory ACLs/ACEs to Retrieve LAPS Passwords]]
- [[Active Directory Account Enumeration using CrackMapExec]]
- [[Active Directory ACLs/ACEs Password Reset]]
- [[Active Directory Assessment and Privilege Escalation]]
- [[Active Directory Integrated DNS Enumeration]]
- [[Active Directory Recon - Using AD Module]]
- [[Active Directory Recon using BloodHound and Certipy]]
- [[Active Directory Recon with PowerView]]
- [[Active Directory User Enumeration]]
- [[Add Domain Admin to RODC Password Replication Group Procedure]]
- [[AdminCount Abuse]]
- [[Analyze BloodHound Data for Relationships]]
- [[Azure Reconnaissance]]
- [[Azure Subdomain Enumeration]]
- [[Domain Admins Group Access]]
- [[Domain Takeover via Certifried CVE-2022-26923]]
- [[Establishing and Enumerating PAM Trust between lab.local and bastion.local]]
- [[Forest to Forest Trust Ticket Hash Dump]]
- [[Forest Trust Ticket Dumping]]
- [[Golden Certificate Domain Persistence]]

*...and 8 more*
