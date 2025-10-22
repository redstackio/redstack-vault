---
id: adf2ad8f-04a2-4d7d-9af2-88a4445f6209
name: Inhibit System Recovery
type: technique
mitre_id: T1490
mitre_url: null
created_at: '2019-08-28T21:17:39.745279+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Impact|TA0040 - Impact]]'
procedures:
- '[[Abusing Backup Operators Group for Sensitive File Access]]'
- '[[Abusing coredumps and core_pattern in Docker containers]]'
- '[[Abusing Shadow Copies for Privilege Escalation]]'
- '[[Copying EC2 Instances using AMI Image in AWS]]'
---

# Inhibit System Recovery

**MITRE ID**: T1490

## Description

Adversaries may delete or remove built-in operating system data and turn off services designed to aid in the recovery of a corrupted system to prevent recovery.[1][2] Operating systems may contain features that can help fix corrupted systems, such as a backup catalog, volume shadow copies, and automatic repair features. Adversaries may disable or delete system recovery features to augment the effects of Data Destruction and Data Encrypted for Impact.[1][2]A number of native Windows utilities have been used by adversaries to disable or delete system recovery features:vssadmin.exe can be used to delete all volume shadow copies on a system - vssadmin.exe delete shadows /all /quietWindows Management Instrumentation can be used to delete volume shadow copies - wmic shadowcopy deletewbadmin.exe can be used to delete the Windows Backup Catalog - wbadmin.exe delete catalog -quietbcdedit.exe can be used to disable automatic Windows recovery features by modifying boot configuration data - bcdedit.exe /set {default} bootstatuspolicy ignoreallfailures & bcdedit /set {default} recoveryenabled no

# Detection

Use process monitoring to monitor the execution and command line parameters of binaries involved in inhibiting system recovery, such as vssadmin, wbadmin, and bcdedit. The Windows event logs, ex. Event ID 524 indicating a system catalog was deleted, may contain entries associated with suspicious activity.

Monitor the status of services involved in system recovery. Monitor the registry for changes associated with system recovery features (ex: the creation of HKEY_CURRENT_USER\Software\Policies\Microsoft\PreviousVersions\DisableLocalPage).

# Mitigation

Consider technical controls to prevent the disabling of services or deletion of files involved in system recovery. 

Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.[6] Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery.

Identify potentially malicious software and audit and/or block it by using whitelisting[7] tools, like AppLocker,[8][9] or Software Restriction Policies[10] where appropriate.[11]

# Footnotes

[1] Mercer, W. and Rascagneres, P. (2018, February 12). Olympic Destroyer Takes Aim At Winter Olympics. Retrieved March 14, 2019.

[2] Berry, A., Homan, J., and Eitzman, R. (2017, May 23). WannaCry Malware Profile. Retrieved March 15, 2019.

[3] Reynolds, J.. (2016, September 14). H1N1: Technical analysis reveals new capabilities – part 2. Retrieved September 26, 2016.

[4] Noerenberg, E., Costis, A., and Quist, N. (2017, May 16). A Technical Analysis of WannaCry Ransomware. Retrieved March 25, 2019.

[5] Counter Threat Unit Research Team. (2017, May 18). WCry Ransomware Analysis. Retrieved March 26, 2019.

[6] Ready.gov. (n.d.). IT Disaster Recovery Plan. Retrieved March 15, 2019.

[7] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[8] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[9] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[10] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[11] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Consider technical controls to prevent the disabling of services or deletion of files involved in system recovery. 

Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organ

## Tactics

- [[Impact|TA0040 - Impact]]

## Related Procedures (4)

- [[Abusing Backup Operators Group for Sensitive File Access]]
- [[Abusing coredumps and core_pattern in Docker containers]]
- [[Abusing Shadow Copies for Privilege Escalation]]
- [[Copying EC2 Instances using AMI Image in AWS]]
