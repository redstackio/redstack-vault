---
id: 4cec8d68-b8f9-411d-ba56-6a250212d965
name: Data Encrypted for Impact
type: technique
mitre_id: T1486
mitre_url: null
created_at: '2019-08-28T21:17:47.937565+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Impact|TA0040 - Impact]]'
procedures:
- '[[Active Directory Account Enumeration using CrackMapExec]]'
- '[[Active Directory User Enumeration]]'
---

# Data Encrypted for Impact

**MITRE ID**: T1486

## Description

Adversaries may encrypt data on target systems or on large numbers of systems in a network to interrupt availability to system and network resources. They can attempt to render stored data inaccessible by encrypting files or data on local and remote drives and withholding access to a decryption key. This may be done in order to extract monetary compensation from a victim in exchange for decryption or a decryption key (ransomware) or to render data permanently inaccessible in cases where the key is not saved or transmitted.[1][2][3][4] In the case of ransomware, it is typical that common user files like Office documents, PDFs, images, videos, audio, text, and source code files will be encrypted. In some cases, adversaries may encrypt critical system files, disk partitions, and the MBR.[3]To maximize impact on the target organization, malware designed for encrypting data may have worm-like features to propagate across a network by leveraging other attack techniques like Valid Accounts, Credential Dumping, and Windows Admin Shares.[2][3]

# Detection

Use process monitoring to monitor the execution and command line parameters of of binaries involved in data destruction activity, such as vssadmin, wbadmin, and bcdedit. Monitor for the creation of suspicious files as well as unusual file modification activity. In particular, look for large quantities of file modifications in user directories.

In some cases, monitoring for unusual kernel driver installation activity can aid in detection.

# Mitigation

Consider implementing IT disaster recovery plans that contain procedures for regularly taking and testing data backups that can be used to restore organizational data.[14]

In some cases, the means to decrypt files affected by a ransomware campaign is released to the public. Research trusted sources for public releases of decryptor tools/keys to reverse the effects of ransomware.

Identify potentially malicious software and audit and/or block it by using whitelisting[15] tools, like AppLocker,[16][17] or Software Restriction Policies[18] where appropriate.[19]

# Footnotes

[1] US-CERT. (2016, March 31). Alert (TA16-091A): Ransomware and Recent Variants. Retrieved March 15, 2019.

[2] Berry, A., Homan, J., and Eitzman, R. (2017, May 23). WannaCry Malware Profile. Retrieved March 15, 2019.

[3] US-CERT. (2017, July 1). Alert (TA17-181A): Petya Ransomware. Retrieved March 15, 2019.

[4] US-CERT. (2018, December 3). Alert (AA18-337A): SamSam Ransomware. Retrieved March 15, 2019.

[5] FireEye. (2018, October 03). APT38: Un-usual Suspects. Retrieved November 6, 2018.

[6] undefined. (2019, March 22). TAU Threat Intelligence Notification – LockerGoga Ransomware. Retrieved April 16, 2019.

[7] Harbison, M.. (2019, March 26). Born This Way? Origins of LockerGoga. Retrieved April 16, 2019.

[8] Chiu, A. (2016, June 27). New Ransomware Variant "Nyetya" Compromises Systems Worldwide. Retrieved March 26, 2019.

[9]  Palotay, D. and Mackenzie, P. (2018, April). SamSam Ransomware Chooses Its Targets Carefully. Retrieved April 15, 2019.

[10] Falcone, R.. (2016, November 30). Shamoon 2: Return of the Disttrack Wiper. Retrieved January 11, 2017.

[11] Falcone, R. (2018, December 13). Shamoon 3 Targets Oil and Gas Organization. Retrieved March 14, 2019.

[12] Noerenberg, E., Costis, A., and Quist, N. (2017, May 16). A Technical Analysis of WannaCry Ransomware. Retrieved March 25, 2019.

[13] Counter Threat Unit Research Team. (2017, May 18). WCry Ransomware Analysis. Retrieved March 26, 2019.

[14] Ready.gov. (n.d.). IT Disaster Recovery Plan. Retrieved March 15, 2019.

[15] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[16] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[17] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[18] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[19] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Consider implementing IT disaster recovery plans that contain procedures for regularly taking and testing data backups that can be used to restore organizational data.(Citation: Ready.gov IT DRP)

In some cases, the means to decrypt files affected by a ra

## Tactics

- [[Impact|TA0040 - Impact]]

## Related Procedures (2)

- [[Active Directory Account Enumeration using CrackMapExec]]
- [[Active Directory User Enumeration]]
