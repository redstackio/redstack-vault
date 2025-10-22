---
id: 3abc0f9a-b749-473e-a173-79200631ea33
name: Disk Structure Wipe
type: technique
mitre_id: T1487
mitre_url: null
created_at: '2019-08-28T21:17:31.607337+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Impact|TA0040 - Impact]]'
---

# Disk Structure Wipe

**MITRE ID**: T1487

## Description

Adversaries may corrupt or wipe the disk data structures on hard drive necessary to boot systems; targeting specific critical systems as well as a large number of systems in a network to interrupt availability to system and network resources. Adversaries may attempt to render the system unable to boot by overwriting critical data located in structures such as the master boot record (MBR) or partition table.[1][2][3][4][5] The data contained in disk structures may include the initial executable code for loading an operating system or the location of the file system partitions on disk. If this information is not present, the computer will not be able to load an operating system during the boot process, leaving the computer unavailable. Disk Structure Wipe may be performed in isolation, or along with Disk Content Wipe if all sectors of a disk are wiped.To maximize impact on the target organization, malware designed for destroying disk structures may have worm-like features to propagate across a network by leveraging other techniques like Valid Accounts, Credential Dumping, and Windows Admin Shares.[1][2][3][4]

# Detection

Look for attempts to read/write to sensitive locations like the master boot record and the disk partition table. Monitor for unusual kernel driver installation activity.

# Mitigation

Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.[11] Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery.

Identify potentially malicious software and audit and/or block it by using whitelisting[12] tools, like AppLocker,[13][14] or Software Restriction Policies[15] where appropriate.[16]

# Footnotes

[1] Symantec. (2012, August 16). The Shamoon Attacks. Retrieved March 14, 2019.

[2] FireEye. (2016, November 30). FireEye Responds to Wave of Destructive Cyber Attacks in Gulf Region. Retrieved January 11, 2017.

[3] Falcone, R.. (2016, November 30). Shamoon 2: Return of the Disttrack Wiper. Retrieved January 11, 2017.

[4] Kaspersky Lab. (2017, March 7). From Shamoon to StoneDrill: Wipers attacking Saudi organizations and beyond. Retrieved March 14, 2019.

[5] Falcone, R. (2018, December 13). Shamoon 3 Targets Oil and Gas Organization. Retrieved March 14, 2019.

[6] FireEye. (2018, February 20). APT37 (Reaper): The Overlooked North Korean Actor. Retrieved March 1, 2018.

[7] Mercer, W., Rascagneres, P. (2018, January 16). Korea In The Crosshairs. Retrieved May 21, 2018.

[8] FireEye. (2018, October 03). APT38: Un-usual Suspects. Retrieved November 6, 2018.

[9] US-CERT. (2018, March 09). Malware Analysis Report (MAR) - 10135536.11.WHITE. Retrieved June 13, 2018.

[10] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.

[11] Ready.gov. (n.d.). IT Disaster Recovery Plan. Retrieved March 15, 2019.

[12] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[13] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[14] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[15] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[16] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Tactics

- [[Impact|TA0040 - Impact]]
