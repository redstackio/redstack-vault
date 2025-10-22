---
id: fdca63f7-0c54-43ca-9d78-94e7301c87fa
name: Pass the Ticket
type: technique
mitre_id: T1097
mitre_url: null
created_at: '2019-08-28T21:17:38.569183+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
procedures:
- '[[Active Directory Assessment and Privilege Escalation]]'
- '[[Active Directory Man-in-the-Middle and Password Cracking]]'
- '[[Active Directory Trust Ticket Forgery with Mimikatz]]'
- '[[AD CS Relay Attack with Rubeus and PetitPotam]]'
- '[[Azure AD Connect - Silver Ticket Attack]]'
- '[[Azure Pass The PRT with Mimikatz]]'
- '[[Create a Golden Ticket and Launch a Windows Shell (Windows)]]'
- '[[Create a Golden Ticket and Launch a Windows SYSTEM Shell (Linux)]]'
- '[[Credential Dumping and Golden Ticket Creation with Metasploit and Mimikatz]]'
- '[[Establishing and Enumerating PAM Trust between lab.local and bastion.local]]'
- '[[Forest to Forest Compromise - Trust Ticket TGS Retrieval and LDAP Authentication]]'
- '[[Forest Trust Ticket Dumping]]'
- '[[GMSA Password Forging]]'
- '[[Golden Ticket Creation via Kerberos Purge]]'
- '[[Golden Ticket Generation with Mimikatz]]'
- '[[Golden Ticket Kerberos Attack on Linux]]'
- '[[NTLM Relay Attack against Active Directory Certificate Services]]'
- '[[Pass-The-Certificate Attack]]'
- '[[Pass-the-Ticket Sapphire Tickets Attack]]'
- '[[Pass-the-Ticket Silver Ticket Creation]]'
- '[[WebDAV Relay Attack]]'
---

# Pass the Ticket

**MITRE ID**: T1097

## Description

Pass the ticket (PtT) is a method of authenticating to a system using Kerberos tickets without having access to an account's password. Kerberos authentication can be used as the first step to lateral movement to a remote system.In this technique, valid Kerberos tickets for Valid Accounts are captured by Credential Dumping. A user's service tickets or ticket granting ticket (TGT) may be obtained, depending on the level of access. A service ticket allows for access to a particular resource, whereas a TGT can be used to request service tickets from the Ticket Granting Service (TGS) to access any resource the user has privileges to access. [1] [2]Silver Tickets can be obtained for services that use Kerberos as an authentication mechanism and are used to generate tickets to access that particular resource and the system that hosts the resource (e.g., SharePoint). [1]Golden Tickets can be obtained for the domain using the Key Distribution Service account KRBTGT account NTLM hash, which enables generation of TGTs for any account in Active Directory. [3]

# Detection

Audit all Kerberos authentication and credential use events and review for discrepancies. Unusual remote authentication events that correlate with other suspicious activity (such as writing and executing binaries) may indicate malicious activity.

Event ID 4769 is generated on the Domain Controller when using a golden ticket after the KRBTGT password has been reset twice, as mentioned in the mitigation section. The status code 0x1F indicates the action has failed due to "Integrity check on decrypted field failed" and indicates misuse by a previously invalidated golden ticket. [14]

# Mitigation

Monitor domains for unusual credential logons. Limit credential overlap across systems to prevent the damage of credential compromise. Ensure that local administrator accounts have complex, unique passwords. Do not allow a user to be a local administrator for multiple systems. Limit domain admin account permissions to domain controllers and limited servers. Delegate other admin functions to separate accounts. [1]

For containing the impact of a previously generated golden ticket, reset the built-in KRBTGT account password twice, which will invalidate any existing golden tickets that have been created with the KRBTGT hash and other Kerberos tickets derived from it. [14]

Attempt to identify and block unknown or malicious software that could be used to obtain Kerberos tickets and use them to authenticate by using whitelisting [15] tools, like AppLocker, [16] [17] or Software Restriction Policies [18] where appropriate. [19]

# Footnotes

[1] Metcalf, S. (2014, November 22). Mimikatz and Active Directory Kerberos Attacks. Retrieved June 2, 2016.

[2] Deply, B. (2014, January 13). Pass the ticket. Retrieved June 2, 2016.

[3] Campbell, C. (2014). The Secret Life of Krbtgt. Retrieved December 4, 2014.

[4] Dunwoody, M. and Carr, N.. (2016, September 27). No Easy Breach DerbyCon 2016. Retrieved October 4, 2016.

[5] Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.

[6] Counter Threat Unit Research Team. (2017, October 12). BRONZE BUTLER Targets Japanese Enterprises. Retrieved January 4, 2018.

[7] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[8] Smallridge, R. (2018, March 10). APT15 is alive and strong: An analysis of RoyalCli and RoyalDNS. Retrieved April 4, 2018.

[9] Metcalf, S. (2015, November 13). Unofficial Guide to Mimikatz & Command Reference. Retrieved December 23, 2015.

[10] Metcalf, S. (2015, August 7). Kerberos Golden Tickets are Now More Golden. Retrieved December 1, 2017.

[11] Schroeder, W. (2015, September 22). Mimikatz and DCSync and ExtraSids, Oh My. Retrieved December 4, 2017.

[12] The Australian Cyber Security Centre (ACSC), the Canadian Centre for Cyber Security (CCCS), the New Zealand National Cyber Security Centre (NZ NCSC), CERT New Zealand, the UK National Cyber Security Centre (UK NCSC) and the US National Cybersecurity and Communications Integration Center (NCCIC). (2018, October 11). Joint report on publicly available hacking tools. Retrieved March 11, 2019.

[13] Symantec Security Response. (2015, July 13). “Forkmeiamfamous”: Seaduke, latest weapon in the Duke armory. Retrieved July 22, 2015.

[14] Abolins, D., Boldea, C., Socha, K., Soria-Machado, M. (2016, April 26). Kerberos Golden Ticket Protection. Retrieved July 13, 2017.

[15] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[16] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[17] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[18] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[19] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Monitor domains for unusual credential logons. Limit credential overlap across systems to prevent the damage of credential compromise. Ensure that local administrator accounts have complex, unique passwords. Do not allow a user to be a local administrator

## Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

## Related Procedures (21)

- [[Active Directory Assessment and Privilege Escalation]]
- [[Active Directory Man-in-the-Middle and Password Cracking]]
- [[Active Directory Trust Ticket Forgery with Mimikatz]]
- [[AD CS Relay Attack with Rubeus and PetitPotam]]
- [[Azure AD Connect - Silver Ticket Attack]]
- [[Azure Pass The PRT with Mimikatz]]
- [[Create a Golden Ticket and Launch a Windows Shell (Windows)]]
- [[Create a Golden Ticket and Launch a Windows SYSTEM Shell (Linux)]]
- [[Credential Dumping and Golden Ticket Creation with Metasploit and Mimikatz]]
- [[Establishing and Enumerating PAM Trust between lab.local and bastion.local]]
- [[Forest to Forest Compromise - Trust Ticket TGS Retrieval and LDAP Authentication]]
- [[Forest Trust Ticket Dumping]]
- [[GMSA Password Forging]]
- [[Golden Ticket Creation via Kerberos Purge]]
- [[Golden Ticket Generation with Mimikatz]]
- [[Golden Ticket Kerberos Attack on Linux]]
- [[NTLM Relay Attack against Active Directory Certificate Services]]
- [[Pass-The-Certificate Attack]]
- [[Pass-the-Ticket Sapphire Tickets Attack]]
- [[Pass-the-Ticket Silver Ticket Creation]]

*...and 1 more*
