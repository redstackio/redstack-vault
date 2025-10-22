---
id: 5ddbbdc0-0d0c-4466-8d31-b0efba0985b3
name: File System Logical Offsets
type: technique
mitre_id: T1006
mitre_url: null
created_at: '2019-08-28T21:17:42.014798+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# File System Logical Offsets

**MITRE ID**: T1006

## Description

Windows allows programs to have direct access to logical volumes. Programs with direct access may read and write files directly from the drive by analyzing file system data structures. This technique bypasses Windows file access controls as well as file system monitoring tools. [1]Utilities, such as NinjaCopy, exist to perform these actions in PowerShell. [2]

# Detection

Monitor handle opens on drive volumes that are made by processes to determine when they may directly access logical drives. [2]

Monitor processes and command-line arguments for actions that could be taken to copy files from the logical drive and evade common file system protections. Since this technique may also be used through PowerShell, additional logging of PowerShell scripts is recommended.

# Mitigation

Identify potentially malicious software that may be used to access logical drives in this manner, and audit and/or block it by using whitelisting [3] tools, like AppLocker, [4] [5] or Software Restriction Policies [6] where appropriate. [7]

# Footnotes

[1] Hakobyan, A. (2009, January 8). FDump - Dumping File Sectors Directly from Disk using Logical Offsets. Retrieved November 12, 2014.

[2] Bialek, J. (2015, December 16). Invoke-NinjaCopy.ps1. Retrieved June 2, 2016.

[3] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[4] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[5] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[6] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[7] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Identify potentially malicious software that may be used to access logical drives in this manner, and audit and/or block it by using whitelisting (Citation: Beechey 2010) tools, like AppLocker, (Citation: Windows Commands JPCERT) (Citation: NSA MS AppLock

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
