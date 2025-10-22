---
id: 78e08b26-2874-4c4c-b2a0-a4b9f8895013
name: Data Destruction
type: technique
mitre_id: T1485
mitre_url: null
created_at: '2019-08-28T21:17:43.017695+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Impact|TA0040 - Impact]]'
procedures:
- '[[Abusing Group Policy Objects with StandIn to Manage Local Administrators and
  User Rights]]'
- '[[AWS Delete EBS Volumes]]'
- '[[AWS Delete File from S3 Bucket]]'
---

# Data Destruction

**MITRE ID**: T1485

## Description

Adversaries may destroy data and files on specific systems or in large numbers on a network to interrupt availability to systems, services, and network resources. Data destruction is likely to render stored data irrecoverable by forensic techniques through overwriting files or data on local and remote drives.[1][2][3][4][5][6] Common operating system file deletion commands such as del and rm often only remove pointers to files without wiping the contents of the files themselves, making the files recoverable by proper forensic methodology. This behavior is distinct from Disk Content Wipe and Disk Structure Wipe because individual files are destroyed rather than sections of a storage disk or the disk's logical structure.Adversaries may attempt to overwrite files and directories with randomly generated data to make it irrecoverable.[4][5] In some cases politically oriented image files have been used to overwrite data.[2][3][4]To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware designed for destroying data may have worm-like features to propagate across a network by leveraging additional techniques like Valid Accounts, Credential Dumping, and Windows Admin Shares.[1][2][3][4][6]

# Detection

Use process monitoring to monitor the execution and command-line parameters of binaries that could be involved in data destruction activity, such as SDelete. Monitor for the creation of suspicious files as well as high unusual file modification activity. In particular, look for large quantities of file modifications in user directories and under C:\Windows\System32\.

# Mitigation

Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.[14] Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery.

Identify potentially malicious software and audit and/or block it by using whitelisting[15] tools, like AppLocker,[16][17] or Software Restriction Policies[18] where appropriate.[19]

# Footnotes

[1] Symantec. (2012, August 16). The Shamoon Attacks. Retrieved March 14, 2019.

[2] FireEye. (2016, November 30). FireEye Responds to Wave of Destructive Cyber Attacks in Gulf Region. Retrieved January 11, 2017.

[3] Falcone, R.. (2016, November 30). Shamoon 2: Return of the Disttrack Wiper. Retrieved January 11, 2017.

[4] Kaspersky Lab. (2017, March 7). From Shamoon to StoneDrill: Wipers attacking Saudi organizations and beyond. Retrieved March 14, 2019.

[5] Falcone, R. (2018, December 13). Shamoon 3 Targets Oil and Gas Organization. Retrieved March 14, 2019.

[6] Mercer, W. and Rascagneres, P. (2018, February 12). Olympic Destroyer Takes Aim At Winter Olympics. Retrieved March 14, 2019.

[7] FireEye. (2018, October 03). APT38: Un-usual Suspects. Retrieved November 6, 2018.

[8] Baumgartner, K. and Garnaeva, M.. (2015, February 17). BE2 extraordinary plugins, Siemens targeting, dev fails. Retrieved March 24, 2016.

[9] Levene, B, et al. (2017, May 03). Kazuar: Multiplatform Espionage Backdoor with API Access. Retrieved July 17, 2018.

[10] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.

[11] Adair, S.. (2016, November 9). PowerDuke: Widespread Post-Election Spear Phishing Campaigns Targeting Think Tanks and NGOs. Retrieved January 11, 2017.

[12] Sherstobitoff, R., Malhotra, A. (2018, April 24). Analyzing Operation GhostSecret: Attack Seeks to Steal Data Worldwide. Retrieved May 16, 2018.

[13] Russinovich, M. (2016, July 4). SDelete v2.0. Retrieved February 8, 2018.

[14] Ready.gov. (n.d.). IT Disaster Recovery Plan. Retrieved March 15, 2019.

[15] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[16] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[17] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[18] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[19] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Tactics

- [[Impact|TA0040 - Impact]]

## Related Procedures (3)

- [[Abusing Group Policy Objects with StandIn to Manage Local Administrators and User Rights]]
- [[AWS Delete EBS Volumes]]
- [[AWS Delete File from S3 Bucket]]
