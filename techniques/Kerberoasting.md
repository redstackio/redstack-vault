---
id: beb2396c-453a-42d1-9667-8e5602d76234
name: Kerberoasting
type: technique
mitre_id: T1208
mitre_url: null
created_at: '2019-08-28T21:17:22.384703+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[Active Directory Assessment and Privilege Escalation]]'
- '[[Active Directory Trust Ticket Forgery with Mimikatz]]'
- '[[Add SPN to a Domain User and Kerberoast for NTLMv2 Hash]]'
- '[[Drop the MIC - Resource Based Constrained Delegation Attack]]'
- '[[Get TGT of User with "Do Not Require Preauthentication" Set]]'
- '[[Golden Ticket Kerberos Attack on Linux]]'
- '[[Kerberoasting with Rubeus]]'
- '[[Kerberos Unconstrained Delegation via SpoolService Abuse]]'
- '[[Kerberos Unconstrained Delegation via SpoolService Abuse]]'
- '[[Query Domain for SPN and Attempt to Kerberoast (Authenticated)]]'
---

# Kerberoasting

**MITRE ID**: T1208

## Description

Service principal names (SPNs) are used to uniquely identify each instance of a Windows service. To enable authentication, Kerberos requires that SPNs be associated with at least one service logon account (an account specifically tasked with running a service [1]). [2] [3] [4] [5]Adversaries possessing a valid Kerberos ticket-granting ticket (TGT) may request one or more Kerberos ticket-granting service (TGS) service tickets for any SPN from a domain controller (DC). [6] [7] Portions of these tickets may be encrypted with the RC4 algorithm, meaning the Kerberos 5 TGS-REP etype 23 hash of the service account associated with the SPN is used as the private key and is thus vulnerable to offline Brute Force attacks that may expose plaintext credentials. [7] [6] [5]This same attack could be executed using service tickets captured from network traffic. [7]Cracked hashes may enable Persistence, Privilege Escalation, and  Lateral Movement via access to Valid Accounts. [4]

# Detection

Enable Audit Kerberos Service Ticket Operations to log Kerberos TGS service ticket requests. Particularly investigate irregular patterns of activity (ex: accounts making numerous requests, Event ID 4769, within a small time frame, especially if they also request RC4 encryption [Type 0x17]). [1] [7]

# Mitigation

Ensure strong password length (ideally 25+ characters) and complexity for service accounts and that these passwords periodically expire. [7] Also consider using Group Managed Service Accounts or another third party product such as password vaulting. [7]

Limit service accounts to minimal required privileges, including membership in privileged groups such as Domain Administrators. [7]

Enable AES Kerberos encryption (or another stronger encryption algorithm), rather than RC4, where possible. [7]

# Footnotes

[1] Bani, M. (2018, February 23). Detecting Kerberoasting activity using Azure Security Center. Retrieved March 23, 2018.

[2] Microsoft. (n.d.). Service Principal Names. Retrieved March 22, 2018.

[3] Microsoft. (2010, April 13). Service Principal Names (SPNs) SetSPN Syntax (Setspn.exe). Retrieved March 22, 2018.

[4] Medin, T. (2014, November). Attacking Kerberos - Kicking the Guard Dog of Hades. Retrieved March 22, 2018.

[5] Schroeder, W. (2016, November 1). Kerberoasting Without Mimikatz. Retrieved March 23, 2018.

[6] EmpireProject. (2016, October 31). Invoke-Kerberoast.ps1. Retrieved March 22, 2018.

[7] Metcalf, S. (2015, December 31). Cracking Kerberos TGS Tickets Using Kerberoast – Exploiting Kerberos to Compromise the Active Directory Domain. Retrieved March 22, 2018.

[8] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[9] SecureAuth. (n.d.).  Retrieved January 15, 2019.

[10] Schroeder, W. & Hart M. (2016, October 31). Invoke-Kerberoast. Retrieved March 23, 2018.

## Defense

Ensure strong password length (ideally 25+ characters) and complexity for service accounts and that these passwords periodically expire. (Citation: AdSecurity Cracking Kerberos Dec 2015) Also consider using Group Managed Service Accounts or another third 

## Tactics

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures (10)

- [[Active Directory Assessment and Privilege Escalation]]
- [[Active Directory Trust Ticket Forgery with Mimikatz]]
- [[Add SPN to a Domain User and Kerberoast for NTLMv2 Hash]]
- [[Drop the MIC - Resource Based Constrained Delegation Attack]]
- [[Get TGT of User with "Do Not Require Preauthentication" Set]]
- [[Golden Ticket Kerberos Attack on Linux]]
- [[Kerberoasting with Rubeus]]
- [[Kerberos Unconstrained Delegation via SpoolService Abuse]]
- [[Kerberos Unconstrained Delegation via SpoolService Abuse]]
- [[Query Domain for SPN and Attempt to Kerberoast (Authenticated)]]
