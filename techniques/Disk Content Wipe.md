---
id: a1adff9a-26ef-40f0-ae68-4c50734b79cb
name: Disk Content Wipe
type: technique
mitre_id: T1488
mitre_url: null
created_at: '2019-08-28T21:17:33.087176+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Impact|TA0040 - Impact]]'
---

# Disk Content Wipe

**MITRE ID**: T1488

## Description

Adversaries may erase the contents of storage devices on specific systems as well as large numbers of systems in a network to interrupt availability to system and network resources.Adversaries may partially or completely overwrite the contents of a storage device rendering the data irrecoverable through the storage interface.[1][2][3] Instead of wiping specific disk structures or files, adversaries with destructive intent may wipe arbitrary portions of disk content. To wipe disk content, adversaries may acquire direct access to the hard drive in order to overwrite arbitrarily sized portions of disk with random data.[2] Adversaries have been observed leveraging third-party drivers like RawDisk to directly access disk content.[1][2] This behavior is distinct from Data Destruction because sections of the disk erased instead of individual files.To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware used for wiping disk content may have worm-like features to propagate across a network by leveraging additional techniques like Valid Accounts, Credential Dumping, and Windows Admin Shares.[2]

# Detection

Look for attempts to read/write to sensitive locations like the partition boot sector or BIOS parameter block/superblock. Monitor for unusual kernel driver installation activity.

# Mitigation

Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.[4] Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery.

Identify potentially malicious software and audit and/or block it by using whitelisting[5] tools, like AppLocker,[6][7] or Software Restriction Policies[8] where appropriate.[9]

# Footnotes

[1] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.

[2] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Destructive Malware Report. Retrieved March 2, 2016.

[3] Department of Justice. (2018, September 6). Criminal Complaint - United States of America v. PARK JIN HYOK. Retrieved March 29, 2019.

[4] Ready.gov. (n.d.). IT Disaster Recovery Plan. Retrieved March 15, 2019.

[5] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[6] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[7] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[8] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[9] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.(Citation: Ready.gov IT DRP) Ensure backups are stored off system and is protected from common methods

## Tactics

- [[Impact|TA0040 - Impact]]
