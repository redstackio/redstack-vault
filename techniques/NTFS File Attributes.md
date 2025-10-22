---
id: ea905a03-07c8-41ad-807c-dd555d934594
name: NTFS File Attributes
type: technique
mitre_id: T1096
mitre_url: null
created_at: '2019-08-28T21:17:27.865171+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[Embed an Alternate Data Stream (ADS) in a File]]'
- '[[Extract an Alternate Data Stream From a File]]'
- '[[SSH Local Port Forwarding]]'
---

# NTFS File Attributes

**MITRE ID**: T1096

## Description

Every New Technology File System (NTFS) formatted partition contains a Master File Table (MFT) that maintains a record for every file/directory on the partition. [1] Within MFT entries are file attributes, [2] such as Extended Attributes (EA) and Data [known as Alternate Data Streams (ADSs) when more than one Data attribute is present], that can be used to store arbitrary data (and even complete files). [1] [3] [4] [5]Adversaries may store malicious data or binaries in file attribute metadata instead of directly in files. This may be done to evade some defenses, such as static indicator scanning tools and anti-virus. [6] [4]

# Detection

Forensic techniques exist to identify information stored in NTFS EA. [6] Monitor calls to the ZwSetEaFile and ZwQueryEaFile Windows API functions as well as binaries used to interact with EA, [21] [22] and consider regularly scanning for the presence of modified information. [1]

There are many ways to create and interact with ADSs using Windows utilities. Monitor for operations (execution, copies, etc.) with file names that contain colons. This syntax (ex: file.ext:ads[.ext]) is commonly associated with ADSs. [5] [21] [22] For a more exhaustive list of utilities that can be used to execute and create ADSs, see https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f.

The Streams tool of Sysinternals can be used to uncover files with ADSs. The dir /r command can also be used to display ADSs. [14] Many PowerShell commands (such as Get-Item, Set-Item, Remove-Item, and Get-ChildItem) can also accept a -stream parameter to interact with ADSs. [4] [5]

# Mitigation

It may be difficult or inadvisable to block access to EA and ADSs. [5] [14] Efforts should be focused on preventing potentially malicious software from running. Identify and block potentially malicious software that may contain functionality to hide information in EA and ADSs by using whitelisting [15] tools like AppLocker [16] [17] or Software Restriction Policies [18] where appropriate. [19]

Consider adjusting read and write permissions for NTFS EA, though this should be tested to ensure routine OS operations are not impeded. [20]

# Footnotes

[1] Atkinson, J. (2017, July 18). Host-based Threat Modeling & Indicator Design. Retrieved March 21, 2018.

[2] Hughes, J. (2010, August 25). NTFS File Attributes. Retrieved March 21, 2018.

[3] Microsoft. (n.d.). File Streams. Retrieved December 2, 2014.

[4] Arntz, P. (2015, July 22). Introduction to Alternate Data Streams. Retrieved March 21, 2018.

[5] Marlin, J. (2013, March 24). Alternate Data Streams in NTFS. Retrieved March 21, 2018.

[6] Harrell, C. (2012, December 11). Extracting ZeroAccess from NTFS Extended Attributes. Retrieved June 3, 2016.

[7] Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.

[8] LOLBAS. (n.d.). Expand.exe. Retrieved February 19, 2019.

[9] ESET. (2017, August). Gazing at Gazer: Turla’s new second stage backdoor. Retrieved September 14, 2017.

[10] Adair, S.. (2016, November 9). PowerDuke: Widespread Post-Election Spear Phishing Campaigns Targeting Think Tanks and NGOs. Retrieved January 11, 2017.

[11] Brumaghin, E. and Grady, C.. (2017, March 2). Covert Channels and Poor Decisions: The Tale of DNSMessenger. Retrieved March 8, 2017.

[12] Kaspersky Lab's Global Research and Analysis Team. (2014, November 24). THE REGIN PLATFORM NATION-STATE OWNAGE OF GSM NETWORKS. Retrieved December 1, 2014.

[13] Ciubotariu, M. (2014, January 23). Trojan.Zeroaccess.C Hidden in NTFS EA. Retrieved December 2, 2014.

[14] Pravs. (2009, May 25). What you need to know about alternate data streams in windows? Is your Data secure? Can you restore that?. Retrieved March 21, 2018.

[15] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[16] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[17] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[18] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[19] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

[20] Sander, J. (2017, October 12). Attack Step 3: Persistence with NTFS Extended Attributes – File System Attacks. Retrieved March 21, 2018.

[21] Moe, O. (2018, January 14). Putting Data in Alternate Data Streams and How to Execute It. Retrieved June 30, 2018.

[22] Moe, O. (2018, April 11). Putting Data in Alternate Data Streams and How to Execute It - Part 2. Retrieved June 30, 2018.

## Defense

It may be difficult or inadvisable to block access to EA and ADSs. (Citation: Microsoft ADS Mar 2014) (Citation: Symantec ADS May 2009) Efforts should be focused on preventing potentially malicious software from running. Identify and block potentially mal

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures (3)

- [[Embed an Alternate Data Stream (ADS) in a File]]
- [[Extract an Alternate Data Stream From a File]]
- [[SSH Local Port Forwarding]]
