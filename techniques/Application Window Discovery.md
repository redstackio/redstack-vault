---
id: 4ce3d5b8-c81d-4f1f-9da5-c643708e2ca3
name: Application Window Discovery
type: technique
mitre_id: T1010
mitre_url: null
created_at: '2019-08-28T21:17:38.674197+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
procedures:
- '[[BigQuery SQL Injection Attack]]'
- '[[Google BigQuery SQL Injection Detection]]'
- '[[Kubernetes etcd API Enumeration]]'
- '[[MSSQL Instance Discovery]]'
- '[[Network Discovery using Nmap]]'
---

# Application Window Discovery

**MITRE ID**: T1010

## Description

Adversaries may attempt to get a listing of open application windows. Window listings could convey information about how the system is used or give context to information collected by a keylogger.In Mac, this can be done natively with a small AppleScript script.

# Detection

System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as Windows Management Instrumentation and PowerShell.

# Mitigation

Identify unnecessary system utilities or potentially malicious software that may be used to acquire information, and audit and/or block them by using whitelisting [13] tools, like AppLocker, [14] [15] or Software Restriction Policies [16] where appropriate. [17]

# Footnotes

[1] Balanza, M. (2018, April 02). Infostealer.Catchamas. Retrieved July 10, 2018.

[2] Symantec Security Response. (2011, November). W32.Duqu: The precursor to the next Stuxnet. Retrieved September 17, 2015.

[3] Levene, B, et al. (2017, May 03). Kazuar: Multiplatform Espionage Backdoor with API Access. Retrieved July 17, 2018.

[4] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.

[5] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Loaders, Installers and Uninstallers Report. Retrieved March 2, 2016.

[6] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Tools Report. Retrieved March 10, 2016.

[7] Kaspersky Lab's Global Research and Analysis Team. (n.d.). The NetTraveler (aka ‘Travnet’). Retrieved November 12, 2014.

[8] Hayashi, K. (2005, August 18). Backdoor.Darkmoon. Retrieved February 23, 2018.

[9] Adair, S.. (2016, November 9). PowerDuke: Widespread Post-Election Spear Phishing Campaigns Targeting Think Tanks and NGOs. Retrieved January 11, 2017.

[10] Legezo, D. (2019, January 30). Chafer used Remexi malware to spy on Iran-based foreign diplomatic entities. Retrieved April 17, 2019.

[11] Carr, N.. (2017, May 14). Cyber Espionage is Alive and Well: APT32 and the Threat to Global Corporations. Retrieved June 18, 2017.

[12] FireEye. (2018, February 20). APT37 (Reaper): The Overlooked North Korean Actor. Retrieved March 1, 2018.

[13] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[14] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[15] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[16] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[17] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Identify unnecessary system utilities or potentially malicious software that may be used to acquire information, and audit and/or block them by using whitelisting (Citation: Beechey 2010) tools, like AppLocker, (Citation: Windows Commands JPCERT) (Citatio

## Tactics

- [[Discovery|TA0007 - Discovery]]

## Related Procedures (5)

- [[BigQuery SQL Injection Attack]]
- [[Google BigQuery SQL Injection Detection]]
- [[Kubernetes etcd API Enumeration]]
- [[MSSQL Instance Discovery]]
- [[Network Discovery using Nmap]]
