---
id: 2794db00-f379-4041-a526-578dd49bb5ba
name: Email Collection
type: technique
mitre_id: T1114
mitre_url: null
created_at: '2019-08-28T21:17:47.702606+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
procedures:
- '[[Creating and Importing a CLR Assembly for MSSQL Server]]'
- '[[Linux Privilege Escalation - Writable Files Escalation]]'
- '[[MSSQL Server Password Retrieval and Cracking]]'
- '[[SAML Injection for Authentication Bypass and Signature Stripping with Admin NameID]]'
---

# Email Collection

**MITRE ID**: T1114

## Description

Adversaries may target user email to collect sensitive information from a target.Files containing email data can be acquired from a user's system, such as Outlook storage or cache files .pst and .ost.Adversaries may leverage a user's credentials and interact directly with the Exchange server to acquire information from within a network.Some adversaries may acquire user credentials and access externally facing webmail applications, such as Outlook Web Access.

# Detection

There are likely a variety of ways an adversary could collect email from a target, each with a different mechanism for detection.

File access of local system email files for Exfiltration, unusual processes connecting to an email server within a network, or unusual access patterns or authentication attempts on a public-facing webmail server may all be indicators of malicious activity.

Monitor processes and command-line arguments for actions that could be taken to gather local email files. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as Windows Management Instrumentation and PowerShell.

# Mitigation

Use of encryption provides an added layer of security to sensitive information sent over email. Encryption using public key cryptography requires the adversary to obtain the private certificate along with an encryption key to decrypt messages.

Use of two-factor authentication for public-facing webmail servers is also a recommended best practice to minimize the usefulness of user names and passwords to adversaries.

Identify unnecessary system utilities or potentially malicious software that may be used to collect email data files or access the corporate email server, and audit and/or block them by using whitelisting [20] tools, like AppLocker, [21] [22] or Software Restriction Policies [23] where appropriate. [24]

# Footnotes

[1] Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.

[2] Mueller, R. (2018, July 13). Indictment - United States of America vs. VIKTOR BORISOVICH NETYKSHO, et al. Retrieved September 13, 2018.

[3] Symantec Security Response. (2014, July 7). Dragonfly: Cyberespionage Attacks Against Energy Suppliers. Retrieved April 8, 2016.

[4] Bennett, J., Vengerik, B. (2017, June 12). Behind the CARBANAK Backdoor. Retrieved June 11, 2018.

[5] F-Secure Labs. (2014, July). COSMICDUKE Cosmu with a twist of MiniDuke. Retrieved July 3, 2014.

[6] Huss, D.. (2016, March 1). Operation Transparent Tribe. Retrieved June 8, 2016.

[7] US-CERT. (2017, October 20). Alert (TA17-293A): Advanced Persistent Threat Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved November 2, 2017.

[8] CIS. (2018, December 12). MS-ISAC Security Primer- Emotet. Retrieved March 25, 2019.

[9] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[10] Vengerik, B. et al.. (2014, December 5). Hacking the Street? FIN4 Likely Playing the Market. Retrieved December 17, 2018.

[11] Vengerik, B. & Dennesen, K.. (2014, December 5). Hacking the Street?  FIN4 Likely Playing the Market. Retrieved January 15, 2019.

[12] Smallridge, R. (2018, March 10). APT15 is alive and strong: An analysis of RoyalCli and RoyalDNS. Retrieved April 4, 2018.

[13] Symantec Security Response. (2018, July 25). Leafminer: New Espionage Campaigns Targeting Middle Eastern Regions. Retrieved August 28, 2018.

[14] Mandiant. (2018). Mandiant M-Trends 2018. Retrieved July 9, 2018.

[15] Nicolas Verdier. (n.d.). Retrieved January 29, 2018.

[16] SensePost. (2016, August 18). Ruler: A tool to abuse Exchange services. Retrieved February 4, 2019.

[17] Symantec Security Response. (2015, July 13). “Forkmeiamfamous”: Seaduke, latest weapon in the Duke armory. Retrieved July 22, 2015.

[18] Baker, B., Unterbrink H. (2018, July 03). Smoking Guns - Smoke Loader learned new tricks. Retrieved July 5, 2018.

[19] Anthony, N., Pascual, C.. (2018, November 1). Trickbot Shows Off New Trick: Password Grabber Module. Retrieved November 16, 2018.

[20] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[21] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[22] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[23] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[24] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Use of encryption provides an added layer of security to sensitive information sent over email. Encryption using public key cryptography requires the adversary to obtain the private certificate along with an encryption key to decrypt messages.

Use of two

## Tactics

- [[Collection|TA0009 - Collection]]

## Related Procedures (4)

- [[Creating and Importing a CLR Assembly for MSSQL Server]]
- [[Linux Privilege Escalation - Writable Files Escalation]]
- [[MSSQL Server Password Retrieval and Cracking]]
- [[SAML Injection for Authentication Bypass and Signature Stripping with Admin NameID]]
