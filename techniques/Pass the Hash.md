---
id: 388d4234-495f-48b5-8d3e-c20f2f1b4dc7
name: Pass the Hash
type: technique
mitre_id: T1075
mitre_url: null
created_at: '2019-08-28T21:17:44.428763+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
procedures:
- '[[Active Directory Man-in-the-Middle and Password Cracking]]'
- '[[AD CS Relay Attack with Rubeus and PetitPotam]]'
- '[[Add Domain Admin to RODC Password Replication Group Procedure]]'
- '[[Browse SMB Share (NTLM)]]'
- '[[Connect to WinRM from a Linux System (Pass-the-Hash)]]'
- '[[Disable LLMNR and NetBIOS over TCP/IP]]'
- '[[Drop the MIC - Resource Based Constrained Delegation Attack]]'
- '[[Execute Commands with an Active Directory Machine Account]]'
- '[[Net-NTLMv1/NTLMv1 Hash Capture and Crack]]'
- '[[Net-NTLMv2/NTLMv2 Hash Capture and Cracking]]'
- '[[NTLM Relay Attack against Active Directory Certificate Services]]'
- '[[OverPass-the-Hash with Impacket]]'
- '[[OverPass-the-Hash with Rubeus]]'
- '[[Pass-the-Hash Active Directory Attack]]'
- '[[Pass the Hash with Meterpreter]]'
- '[[Pass The Hash with Mimikatz]]'
- '[[samAccountName Spoofing Attack]]'
- '[[Skeleton Key Password Injection]]'
- '[[Windows Credentials Impacket Commands]]'
- '[[Windows - Impacket Psexec Remote Command Execution]]'
- '[[Windows SSH with Kerberos Authentication]]'
- '[[Windows - Using Impacket and PSExec with Credentials]]'
- '[[Workstation Takeover with RBCD]]'
---

# Pass the Hash

**MITRE ID**: T1075

## Description

Pass the hash (PtH) is a method of authenticating as a user without having access to the user's cleartext password. This method bypasses standard authentication steps that require a cleartext password, moving directly into the portion of the authentication that uses the password hash. In this technique, valid password hashes for the account being used are captured using a Credential Access technique. Captured hashes are used with PtH to authenticate as that user. Once authenticated, PtH may be used to perform actions on local or remote systems. Windows 7 and higher with KB2871997 require valid domain user credentials or RID 500 administrator hashes. [1]

# Detection

Audit all logon and credential use events and review for discrepancies. Unusual remote logins that correlate with other suspicious activity (such as writing and executing binaries) may indicate malicious activity. NTLM LogonType 3 authentications that are not associated to a domain login and are not anonymous logins are suspicious.

# Mitigation

Monitor systems and domain logs for unusual credential logon activity. Prevent access to Valid Accounts. Apply patch KB2871997 to Windows 7 and higher systems to limit the default access of accounts in the local administrator group. 

Enable pass the hash mitigations to apply UAC restrictions to local accounts on network logon. The associated Registry key is located HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\LocalAccountTokenFilterPolicy Through GPO: Computer Configuration > [Policies] > Administrative Templates > SCM: Pass the Hash Mitigations: Apply UAC restrictions to local accounts on network logons. [12]

Limit credential overlap across systems to prevent the damage of credential compromise and reduce the adversary's ability to perform Lateral Movement between systems. Ensure that built-in and created local administrator accounts have complex, unique passwords. Do not allow a domain user to be in the local administrator group on multiple systems.

# Footnotes

[1] National Security Agency/Central Security Service Information Assurance Directorate. (2015, August 7). Spotting the Adversary with Windows Event Log Monitoring. Retrieved September 6, 2018.

[2] Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.

[3] Anthe, C. et al. (2015, October 19). Microsoft Security Intelligence Report Volume 19. Retrieved December 23, 2015.

[4] Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.

[5] Cobalt Strike. (2017, December 8). Tactics, Techniques, and Procedures. Retrieved December 20, 2017.

[6] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[7] US-CERT. (2019, April 10). MAR-10135536-8 – North Korean Trojan: HOPLIGHT. Retrieved April 19, 2019.

[8] Metcalf, S. (2015, November 13). Unofficial Guide to Mimikatz & Command Reference. Retrieved December 23, 2015.

[9] The Australian Cyber Security Centre (ACSC), the Canadian Centre for Cyber Security (CCCS), the New Zealand National Cyber Security Centre (NZ NCSC), CERT New Zealand, the UK National Cyber Security Centre (UK NCSC) and the US National Cybersecurity and Communications Integration Center (NCCIC). (2018, October 11). Joint report on publicly available hacking tools. Retrieved March 11, 2019.

[10] McAfee® Foundstone® Professional Services and McAfee Labs™. (2011, February 10). Global Energy Cyberattacks: “Night Dragon”. Retrieved February 19, 2018.

[11] Nettitude. (2016, June 8). PoshC2: Powershell C2 Server and Implants. Retrieved April 23, 2019.

[12] NSA IAD. (2017, January 24). MS Security Guide. Retrieved December 18, 2017.

## Defense

Monitor systems and domain logs for unusual credential logon activity. Prevent access to [Valid Accounts](https://attack.mitre.org/techniques/T1078). Apply patch KB2871997 to Windows 7 and higher systems to limit the default access of accounts in the loca

## Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

## Related Procedures (23)

- [[Active Directory Man-in-the-Middle and Password Cracking]]
- [[AD CS Relay Attack with Rubeus and PetitPotam]]
- [[Add Domain Admin to RODC Password Replication Group Procedure]]
- [[Browse SMB Share (NTLM)]]
- [[Connect to WinRM from a Linux System (Pass-the-Hash)]]
- [[Disable LLMNR and NetBIOS over TCP/IP]]
- [[Drop the MIC - Resource Based Constrained Delegation Attack]]
- [[Execute Commands with an Active Directory Machine Account]]
- [[Net-NTLMv1/NTLMv1 Hash Capture and Crack]]
- [[Net-NTLMv2/NTLMv2 Hash Capture and Cracking]]
- [[NTLM Relay Attack against Active Directory Certificate Services]]
- [[OverPass-the-Hash with Impacket]]
- [[OverPass-the-Hash with Rubeus]]
- [[Pass-the-Hash Active Directory Attack]]
- [[Pass the Hash with Meterpreter]]
- [[Pass The Hash with Mimikatz]]
- [[samAccountName Spoofing Attack]]
- [[Skeleton Key Password Injection]]
- [[Windows Credentials Impacket Commands]]
- [[Windows - Impacket Psexec Remote Command Execution]]

*...and 3 more*
